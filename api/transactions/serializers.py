from rest_framework import serializers
from transactions.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'name', 'referer', 'amount', 'date']
        ordering = ['-id']

    def create(self, validated_data):
        balance = 0
        qs = Transaction.objects.filter(name= validated_data['name']).order_by('-date', '-id').first()
        if qs:
            balance = qs.balance

        transaction = Transaction.objects.create(**validated_data, balance=validated_data['amount'] + balance)
        return transaction


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'name', 'date', 'balance']
        ordering = ['-id']


class ProcessCsvSerializer(serializers.Serializer):
    path = serializers.CharField(max_length=200)

