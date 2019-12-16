from rest_framework import serializers
from api.transactions.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'referer', 'amount', 'date']


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'date', 'balance']
