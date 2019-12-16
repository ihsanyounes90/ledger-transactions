from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.transactions.serializers import *


class BalanceView(viewsets.ModelViewSet):
    """
    API endpoint that allows balances to be viewed
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = BalanceSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = TransactionSerializer