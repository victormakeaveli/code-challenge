from rest_framework import viewsets


from .serializers import CustomerSerializer, Credit_CardSerializer, TransactionSerializer, StatusesSerializer, CompanySerializer
from .models import Company, Customer, Credit_Card, Transaction, Statuses


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Credit_CardView(viewsets.ModelViewSet):
    queryset = Credit_Card.objects.all()
    serializer_class = Credit_CardSerializer


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class StatusesView(viewsets.ModelViewSet):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

