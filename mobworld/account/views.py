

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from .forms import*
from .models import CustUser,Product
from django.contrib import messages
from customer.form import*
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.contrib.auth import authenticate,login,logout

# Create your views here.
class HomeView(TemplateView):
    template_name="home.html"

class Reg(CreateView):
    template_name="reg.html"
    form_class=RegForm 
    model=CustUser 
    success_url=reverse_lazy("h")
    def form_valid(self, form):
        mail=form.cleaned_data.get("email")
        send_mail(
            "Around Me Registration",  #subject
            "hi user thank you for registering in mobilestore", #message
            "asharikk99@gmail.com", 
            [mail]
        )
        messages.success(self.request,"registration Successsful")
        self.object=form.save()
        return super().form_valid(form)
class Login(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self, request, *args: str, **kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            store=form_data.cleaned_data.get("Store")

            user=authenticate(request,username=un,password=pw)
            if user:
                if user.usertype == "Customer":
                    print(user.first_name,user.last_name)
                    login(request,user)
                    return redirect('ch')
                elif user.usertype == "Store":
                    return redirect('pro')
            
            
            else:
                return redirect('lg')
                
        else:
            messages.error(request,"login error!! username or password is incorrect")
            return redirect('lg')
            

class ProView(CreateView):
    form_class=ProductForm
    template_name="store.html"
    model=Product 
    success_url=reverse_lazy("pro")
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Product Added!!")
        return super().form_valid(form)
    def get_context_data(self,**kwargs):    
        context=super().get_context_data(**kwargs)
        context["data"]=Product.objects.all()
        return context


class EditProductView(UpdateView):
    form_class=ProductForm
    model=Product
    template_name="editpro.html"
    success_url=reverse_lazy("pro")
    pk_url_kwarg="pk"

class DeleteProduct(DeleteView):
    model=Product
    template_name="delpro.html"
    success_url=reverse_lazy("pro")

class CustomerHome(TemplateView):
    template_name="userhome.html"
    
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["data"]=Product.objects.all
        context["cform"]=ReviewForm()
        context["comments"]=Review.objects.all()
        return context
    # def get_context_data(self,**kwargs):    
    #     context=super().get_context_data(**kwargs)
    #     context["data"]=Product.objects.all().order_by('-datetime')
    #     context["cform"]=ReviewForm()
    #     context["comments"]=Review.objects.all()
    #     return context

class BestView(TemplateView):
    template_name="best.html"
        
class LogOut(View):
    def get(self,req):
        logout(req)
        messages.error(req,"user logged out")
        return redirect("h")


