from rest_framework import serializers
from .models import Portfolio, Trade, Deposit, Wallet, Transaction, Withdrawal, Billing, Notification, Card, Profile


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'


class WithdrawalSerializer(serializers.ModelSerializer):
    billings = BillingSerializer(many=True, required=False)

    class Meta:
        model = Withdrawal
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):
    current = serializers.ReadOnlyField()

    class Meta:
        model = Trade
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    progress = serializers.ReadOnlyField()
    current = serializers.ReadOnlyField()
    wallet = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    referrer = serializers.ReadOnlyField()
    pending_notifications = serializers.ReadOnlyField()
    pending_trades = serializers.ReadOnlyField()
    pending_withdrawals = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
    current = serializers.ReadOnlyField()
    available = serializers.ReadOnlyField()
    btc_total = serializers.ReadOnlyField()
    btc_current = serializers.ReadOnlyField()
    btc_available = serializers.ReadOnlyField()
    eth_total = serializers.ReadOnlyField()
    eth_current = serializers.ReadOnlyField()
    eth_available = serializers.ReadOnlyField()
    ltc_total = serializers.ReadOnlyField()
    ltc_current = serializers.ReadOnlyField()
    ltc_available = serializers.ReadOnlyField()
    xrp_total = serializers.ReadOnlyField()
    xrp_current = serializers.ReadOnlyField()
    xrp_available = serializers.ReadOnlyField()

    class Meta:
        model = Portfolio
        fields = ('id', 'account', 'card', 'profile', 'referrer',
                  'trader_id', 'trade_score', 'full_name',
                  'pending_notifications', 'pending_trades', 'pending_withdrawals',
                  'total', 'current', 'available',
                  'btc_total', 'btc_current', 'btc_available',
                  'eth_total', 'eth_current', 'eth_available',
                  'ltc_total', 'ltc_current', 'ltc_available',
                  'xrp_total', 'xrp_current', 'xrp_available')
        depth = 1

# special cases


class ExpertTraderSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Portfolio
        fields = ('id',  'full_name', 'trader_id', 'trade_score')


class AddTradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = '__all__'


class AddWithdrawalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdrawal
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
