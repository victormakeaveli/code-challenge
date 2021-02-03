from django.urls import include, path
from rest_framework import routers

from . import views
# from .models import CreditCard

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('account', views.AccountView)
router.register('creditcard', views.CreditCardView)
router.register('transaction', views.TransactionView)


urlpatterns = [
    path('', include(router.urls)),
]


# for url in router.urls:
#     print(url, '\n')

# print(CreditCard.objects.filter().explain(verbose=True, analyze=True), '\n')
# print(User.objects.filter().explain(verbose=True, analyze=True), '\n')
# print(Transaction.objects.filter().explain(verbose=True, analyze=True), '\n')

