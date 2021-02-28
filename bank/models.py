
from django.db import models
from django.db.models.fields.related import ForeignKey


class BaseModel(models.Model):
    """
    a base model to keep track of creation and updates
    """

    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True


class Account(BaseModel):
    """
    The bank account model 
    """

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.user)

    __repr__ = __str__


class CreditCard(BaseModel):
    """
    The Credit Card
    """

    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 64)
    card_number = models.CharField(max_length = 64)
    CVV = models.CharField(max_length = 64)
    exp_date = models.DateField()
    limit = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.full_name

    __repr__ = __str__


class User(BaseModel):
    """
    The customer model
    """
    
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 

    __repr__ = __str__


class Transaction(BaseModel):
    """
   The Transaction model
    """

    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('BRL', 'BRL'),
    )


    TRANSACTION_CHOICES = (
        ('paid', 'paid'), 
        ('refunded', 'refunded'),
        ('dispute', 'dispute'),
        ('failed', 'failed'), 
    )

    
    credit_card = models.ForeignKey('CreditCard', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    status = models.CharField(
        max_length=64,
        choices=TRANSACTION_CHOICES,
        default=None,
        null=True,
    )

    currency = models.CharField(
        max_length=64,
        choices=CURRENCY_CHOICES,
        default='USD',
    )


    def __str__(self):
        return str(self.id)

    __repr__ = __str__
