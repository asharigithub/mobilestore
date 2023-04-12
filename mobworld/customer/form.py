from django import forms
from.models import Cart
from .models import Buy
from customer.models import Product,Review



class Quantity(forms.Form):
    quantity=forms.IntegerField()
 



class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Credit Card Number', max_length=16)
    expiration_date = forms.DateField(label='Expiration Date', widget=forms.DateInput(attrs={'type': 'date'}))
    security_code = forms.CharField(label='Security Code', max_length=3)

class OrderForm(forms.Form):
    class Meta:
        model = Buy
        fields = ['name', 'email', 'phone', 'address', 'product']
 # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    # phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))
    # address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}))
    # product = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Product.objects.all())  


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"})
        }