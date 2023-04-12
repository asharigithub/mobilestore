from django import forms
from .models import CustUser,Product
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        
        fields=["first_name","last_name","email","phone","adress","image","usertype","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
    