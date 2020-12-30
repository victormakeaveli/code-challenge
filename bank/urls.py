from django.urls import path, include
from rest_framework import routers

from . import views 


router = routers.DefaultRouter()
router.register('customer', views.CustomerView)
router.register('credit_Card', views.Credit_CardView)
# router.register('transaction', views.TransactionView)
router.register('statuses', views.StatusesView)
router.register('company', views.CompanyView)

urlpatterns = [
    path('', include(router.urls)),
]
