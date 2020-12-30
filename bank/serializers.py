from rest_framework import serializers
from .models import Customer, Credit_Card, Statuses, Transaction, Company



class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name')
    

class StatusesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statuses
        fields = ('status',)

    def __str__(self):
        return Statuses.status()


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class Credit_CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credit_Card
        fields = ('id', 'company', 'customer', 'card_number', 'CVV' ,'exp_date' ,'limit')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('card', 'amount')

    