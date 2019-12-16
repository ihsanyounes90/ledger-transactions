from django.urls import include, path
from rest_framework import routers
from transactions import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet, basename="transactions")
router.register(r'balances', views.BalanceView, basename="balances")

urlpatterns = [
    path('', include(router.urls)),
]
