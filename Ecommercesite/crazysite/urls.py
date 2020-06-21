from django.urls import path
from . import views


urlpatterns=[

    path('',views.index, name ='shop'),
    path('about/',views.aboutus, name ='aboutus'),
    path('contact/',views.contactus, name = 'contactus'),
    path('search/', views.search, name = 'search'),
    path('product/', views.product, name = 'product'),
    path('ordertracking/', views.ordertracking, name = 'ordertracking'),
    path('checkout/', views.checkout, name = 'checkout')

    
] 