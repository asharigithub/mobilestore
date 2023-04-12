
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustUser(AbstractUser):
    phone=models.IntegerField(null=True)
    adress=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to="profile_image",null=True)
    options=(
        ("Store","Store"),
        ("Customer","Customer")
    )
    usertype=models.CharField(max_length=100,choices=options,default="Customer")

BRANDS=(
    ("apple","apple"),
    ("samsung","samsung"),
    ("oneplus","oneplus"),
    ("redmi","redmi"),
    ("realme","realme"),
    ("oppo","oppo")
)

# Create your models here.
class Product(models.Model):
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='p_user',null=True)
    productname = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    discount_price=models.FloatField()
    description = models.TextField()
    brand=models.CharField(choices=BRANDS,max_length=100)
    rating=models.FloatField()
    image = models.ImageField(upload_to='product',null=True) 
    

    def __str__(self):
        return self.productname
