from django.urls import path
from customer.views import *


urlpatterns= [
   
    path('MyCart/',MyCart.as_view(),name="mycart"),
    path('addcart/<int:pid>',addcart,name='addc'),
    path('delcart/<int:pid>',delcart,name='delcart'),
    path('buy/<int:pid>', BuyView.as_view(), name='buy'),
    path('ordersuccess/', OrderSuccessView.as_view(), name='ordersuccess'),
    path('review/<int:pid>/', addreview, name='addr'),
    path('pay/', PaymentView.as_view, name='pay'),
    


]