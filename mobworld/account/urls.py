from django.urls import path 
from .views import*


urlpatterns=[
    path("reg/",Reg.as_view(),name='reg'),
    path('log/',Login.as_view(),name='lg'),
    path('product/',ProView.as_view(),name='pro'),
    path('custhome/',CustomerHome.as_view(),name="ch"),
    path('best/',BestView.as_view(),name="best"),
    path('logout',LogOut.as_view(),name='lgout'),
    path("editproduct/<int:pk>",EditProductView.as_view(),name="epro"),
    path('delproduct/<int:pk>',DeleteProduct.as_view(),name="dpro"),


    
]