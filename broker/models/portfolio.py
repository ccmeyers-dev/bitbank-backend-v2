from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.utils import timezone

Account = get_user_model()


def TraderID():
    return get_random_string(length=8)


class Portfolio(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, blank=True, null=True)
    trader_id = models.CharField(
        max_length=10, default=TraderID, editable=False)
    trade_score = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.account)

    def full_name(self):
        return "{} {}".format(self.account.first_name, self.account.last_name)

    def referrer(self):
        if self.account.referrer:
            try:
                referrer = Portfolio.objects.get(
                    trader_id=self.account.referrer)
                return referrer.account.email
            except:
                return "None"
        return "None"

    def pending_notifications(self):
        return self.notifications.filter(read=False).count()

    def pending_trades(self):
        return self.trades.filter(profit__lte=0).count()

    def pending_withdrawals(self):
        return self.withdrawals.filter(completed=False).count()

    def book(self):
        return sum([deposit.amount for deposit in self.deposits.all()]) - sum([trade.amount for trade in self.trades.all()])

    @property
    def total(self):
        return sum([trade.profit for trade in self.trades.all()]) + self.book()

    @property
    def current(self):
        return sum([trade.current for trade in self.trades.all()]) + self.book()

    @property
    def available(self):
        return sum([trade.current for trade in self.trades.all().filter(withdrawal_date__lte=timezone.now())]) + self.book()
    # end total balance

    # btc balance

    def btc_book(self):
        return sum([deposit.amount for deposit in self.deposits.all().filter(wallet__symbol='BTC')]) - sum([trade.amount for trade in self.trades.all().filter(wallet__symbol='BTC')])

    @property
    def btc_total(self):
        return sum([trade.profit for trade in self.trades.all().filter(wallet__symbol='BTC')]) + self.btc_book()

    @property
    def btc_current(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='BTC')]) + self.btc_book()

    @property
    def btc_available(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='BTC').filter(withdrawal_date__lte=timezone.now())]) + self.btc_book()
    # end btc balance

    # eth balance

    def eth_book(self):
        return sum([deposit.amount for deposit in self.deposits.all().filter(wallet__symbol='ETH')]) - sum([trade.amount for trade in self.trades.all().filter(wallet__symbol='ETH')])

    @property
    def eth_total(self):
        return sum([trade.profit for trade in self.trades.all().filter(wallet__symbol='ETH')]) + self.eth_book()

    @property
    def eth_current(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='ETH')]) + self.eth_book()

    @property
    def eth_available(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='ETH').filter(withdrawal_date__lte=timezone.now())]) + self.eth_book()
    # end eth balance

    # ltc balance

    def ltc_book(self):
        return sum([deposit.amount for deposit in self.deposits.all().filter(wallet__symbol='LTC')]) - sum([trade.amount for trade in self.trades.all().filter(wallet__symbol='LTC')])

    @property
    def ltc_total(self):
        return sum([trade.profit for trade in self.trades.all().filter(wallet__symbol='LTC')]) + self.ltc_book()

    @property
    def ltc_current(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='LTC')]) + self.ltc_book()

    @property
    def ltc_available(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='LTC').filter(withdrawal_date__lte=timezone.now())]) + self.ltc_book()
    # end ltc balances

    # xrp balance

    def xrp_book(self):
        return sum([deposit.amount for deposit in self.deposits.all().filter(wallet__symbol='XRP')]) - sum([trade.amount for trade in self.trades.all().filter(wallet__symbol='XRP')])

    @property
    def xrp_total(self):
        return sum([trade.profit for trade in self.trades.all().filter(wallet__symbol='XRP')]) + self.xrp_book()

    @property
    def xrp_current(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='XRP')]) + self.xrp_book()

    @property
    def xrp_available(self):
        return sum([trade.current for trade in self.trades.all().filter(wallet__symbol='XRP').filter(withdrawal_date__lte=timezone.now())]) + self.xrp_book()
    # end xrp balances
