from django.urls import include, path
from rest_framework import routers
from transactions import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet, "transactions")
router.register(r'balances', views.BalanceView, "balances")

urlpatterns = [
    path('', include(router.urls)),
    path('transactions-csv', views.process_csv, name="transactions-csv"),
]
