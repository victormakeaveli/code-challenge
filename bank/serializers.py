from inspect import Attribute
from rest_framework import fields, serializers

from .models import Account, CreditCard, Transaction, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'first_name',
            'last_name',
            'created',
            'last_modified',
        )


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'url',
            'user',
            'balance',
            'created',
            'last_modified',
        )


class CreditCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CreditCard
        fields = (
            'id',
            'url',
            'account',
            'full_name',
            'card_number',
            'CVV',
            'exp_date',
            'limit',
            'created',
            'last_modified',
        )


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    def validate_status(current_status, new_status):
        if current_status == Transaction.TRANSACTION_CHOICES[0][0] and new_status == Transaction.TRANSACTION_CHOICES[3][0]:
            raise Exception ("can't set a paid status to failed")

        if current_status != Transaction.TRANSACTION_CHOICES[2][0] and new_status == Transaction.TRANSACTION_CHOICES[1][0]:
            raise Exception ("can't refund a transaction without disputing it")
#!      
        if current_status == Transaction.TRANSACTION_CHOICES[3][0] and new_status == Transaction.TRANSACTION_CHOICES[0][0]:
            raise Exception ("can't set a status to failed while paid")
#!
        if current_status == Transaction.TRANSACTION_CHOICES[1][0] and new_status == Transaction.TRANSACTION_CHOICES[2][0]:
            raise Exception ("can't set a refunded transaction back to dispute")

        return new_status

    # based on previous validation function, this assertions will work 
    # assert validate_status('paid', 'dispute') == "dispute"
    # assert validate_status('failed', 'dispute') == "dispute"
    # assert validate_status('dispute', 'refunded') == "refunded"
    # assert validate_status('dispute', 'failed') == "failed"

    # and these must throw an exception error
    # try:
    #     assert validate_status('paid', 'failed')
    # except Exception as error:
    #     print (error)

    # try:
    #     assert validate_status('paid', 'refunded')
    # except Exception as error:
    #     print (error)

    # try:
    #     assert validate_status('refunded', 'dispute')
    # except Exception as error:
    #     print (error)

    class Meta:
        model = Transaction
        fields = (
            'id',
            'url',
            'credit_card',
            'amount',
            'currency',
            'status',
            'created',
            'last_modified',
        )

