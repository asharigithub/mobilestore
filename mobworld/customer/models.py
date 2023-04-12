from django.db import models
from account.models import CustUser,Product


# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='m_cart',null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='u_cart')

class Review(models.Model):
    comment=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='commented_user')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='commented_product')


class Buy(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
