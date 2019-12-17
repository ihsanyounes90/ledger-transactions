from rest_framework import serializers
from transactions.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'name', 'referer', 'amount', 'date']
        ordering = ['-id']

    def create(self, validated_data):

        # referer balance
        balance = 0
        qs = Transaction.objects.filter(name=validated_data['referer']).order_by('-date', '-id').first()
        if qs:
            balance = qs.balance
        transaction = Transaction.objects.create(name=validated_data["referer"], referer=validated_data["name"], date=validated_data["date"],
                                                 amount=validated_data["amount"], balance=validated_data['amount'] + balance)
        transaction.save()

        # current balance
        balance = 0
        qs = Transaction.objects.filter(name=validated_data['name']).order_by('-date', '-id').first()
        if qs:
            balance = qs.balance
        transaction = Transaction.objects.create(name=validated_data["name"], referer=validated_data["referer"], date=validated_data["date"],
                                                 amount=-validated_data["amount"], balance=balance - validated_data['amount'])

        return transaction


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'name', 'date', 'balance']
        ordering = ['-id']


class ProcessCsvSerializer(serializers.Serializer):
    path = serializers.CharField(max_length=200)

