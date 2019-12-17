from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transactions.serializers import *
from transactions.models import Transaction
from tasks import process_csv_task

class BalanceView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows balances to be viewed
    """
    queryset = Transaction.objects.all().order_by('-id')
    serializer_class = BalanceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned balances to a given user,
        by filtering against a `name` query parameter in the URL.
        Further filtering with the balance 'date' is possible
        """
        queryset = Transaction.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        date = self.request.query_params.get('date', None)
        print(self.request.query_params)
        if name is not None:
            queryset = queryset.filter(name=name)
        if date is not None:
            print("filtering by date")
            queryset = queryset.filter(date=date)
        return queryset


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    queryset = Transaction.objects.all().order_by('-id')
    serializer_class = TransactionSerializer


@api_view(['POST'])
def process_csv(request):

    serializer = ProcessCsvSerializer(data=request.data)
    if serializer.is_valid():
        process_csv_task.delay(serializer.validated_data["path"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
