from Husky.pagination import CustomPagination
from rest_framework import status, viewsets
from rest_framework.decorators import action
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Account, CreditCard, Transaction, User
from .serializers import (
        AccountSerializer, CreditCardSerializer, 
        TransactionSerializer,
        UserSerializer,
    )


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CreditCardView(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(methods=['get'], detail=True)
    def last(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class TransactionView(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = CustomPagination

