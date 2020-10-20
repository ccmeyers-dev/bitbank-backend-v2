from django.urls import path, include
from rest_framework import routers
from .views import (
    PortfolioViewSet, TradeViewSet,
    DepositViewSet, WalletViewSet,
    TransactionViewSet, WithdrawalViewSet,
    BillingViewSet, AddWithdrawalViewSet,
    UserProfileView, ExpertTraderViewSet, DeleteCardView,
    SetExpertTraderView, RemoveExpertTraderView,
    AddTradeViewSet, ToggleAdminView, ToggleActiveView,
    DeleteUserView, AdminDashboardView,
    NotificationViewSet, CardView, ProfileView
)

router = routers.SimpleRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'trades', TradeViewSet)
router.register(r'add-trades', AddTradeViewSet)
router.register(r'deposits', DepositViewSet)
router.register(r'withdrawals', WithdrawalViewSet)
router.register(r'billings', BillingViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'expert-traders', ExpertTraderViewSet)
router.register(r'add-withdrawals', AddWithdrawalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view()),
    path('card/', CardView.as_view()),
    path('setup-profile/', ProfileView.as_view()),
    path('admin/', AdminDashboardView.as_view()),
    path('set-expert/<int:pk>/', SetExpertTraderView.as_view()),
    path('remove-expert/<int:pk>/', RemoveExpertTraderView.as_view()),
    path('toggle-admin/<int:pk>/', ToggleAdminView.as_view()),
    path('toggle-active/<int:pk>/', ToggleActiveView.as_view()),
    path('delete-user/<int:pk>/', DeleteUserView.as_view()),
    path('delete-card/<int:pk>/', DeleteCardView.as_view())
]
