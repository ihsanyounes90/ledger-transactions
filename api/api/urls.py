from django.urls import include, path
from rest_framework import routers
from api.transactions import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet)
router.register(r'balances', views.BalanceView)

urlpatterns = [
    path('', include(router.urls)),
]
