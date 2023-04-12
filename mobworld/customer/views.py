from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from .form import*
from account.models import Product
from .models import*



# Create your views here.
def addcart(req,*args,**kwargs):
    id=kwargs.get("pid")
    product=Product.objects.get(id=id)
    user=req.user
    Cart.objects.create(product=product,user=user)
    return redirect('ch')
def delcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    user=request.user
    Cart.objects.filter(id=id).delete()
    return redirect('mycart')

class MyCart(TemplateView):
    template_name='cart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Cart.objects.all()
        return context
    
def addreview(request, pid):
    if request.method=="POST":
        id = pid
        product = Product.objects.get(id=id)
        user = request.user
        cmnt = request.POST.get("comment")
        Review.objects.create(product=product, user=user, comment=cmnt)
        return redirect('ch')
    
class BuyView(TemplateView):
    template_name = 'buy.html'


    def post(self, request, *args, **kwargs):
        user = request.user
        products = Cart.objects.filter(user=user).values_list('product', flat=True)
        total_cost = sum(Product.objects.filter(user=user).values_list('discount_price', flat=True))
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment
            buy = Buy.objects.create(user=user, total_cost=total_cost)
            buy.products.set(products)
            Cart.objects.filter(user=user).delete()
            return redirect('ordersuccess')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)

class PaymentView(FormView):
    template_name = 'payment.html'
    form_class = PaymentForm
    success_url = 'ordersuccess'

    def form_valid(self, form):
        # Process payment
      return super().form_valid(form)        

class OrderSuccessView(TemplateView):
    template_name = 'success.html'