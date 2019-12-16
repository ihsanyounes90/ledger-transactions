from rest_framework import viewsets
from transactions.serializers import *
from transactions.models import Transaction


class BalanceView(viewsets.ModelViewSet):
    """
    API endpoint that allows balances to be viewed
    """
    queryset = Transaction.objects.all().order_by('-id')
    serializer_class = BalanceSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
"""
    def create(self, request):
        # super().create(request)

        serializer = TransactionSerializer(data=request.DATA)
        if serializer.is_valid():
            transaction = serializer.validated_data
            print(transaction)

            transaction = Booking(**serializer.data['booking'])
            transaction.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""