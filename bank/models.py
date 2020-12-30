from django.db import models



class Customer(models.Model):
    """
    Customer
    """
    
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.last_name


class Statuses(models.Model):
    """
    maybe this is naive but it is what I got
    """

    status = models.CharField(max_length=8)
    
    def __str__(self):
        return self.status


class Company(models.Model):
    """
    same purpose of Statuses
    """

    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Credit_Card(models.Model):
    """
    Credit Card
    
    company 
    customer_att    # variable identifying credit cards owner
    card_number
    CVV
    exp_date
    limit
    """
    
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    CVV = models.IntegerField()
    exp_date = models.DateField()
    limit = models.IntegerField()





class Transaction(models.Model):
    """
    the transfer application*
    """


    # card1 = models.OneToOneField(Credit_Card, on_delete=models.CASCADE)
    # card2 = None
    # amount = models.IntegerField()

    # def __str__(self):
    #     return Transaction.id


#**a function to do the computing**#

 
class Attempt(models.Model):
    """
    the information (status per say) about the transaction
    """

    # amount = models.ForeignKey(Transaction.amount(), on_delete=models.CASCADE)
    # status
    # payee 
    # receiver 
    pass