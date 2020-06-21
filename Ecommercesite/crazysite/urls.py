from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('',views.index, name ='shop'),
    path('about/',views.aboutus, name ='aboutus'),
    path('contact/',views.contactus, name = 'contactus'),
    path('search/', views.search, name = 'search'),
    path('product/', views.product, name = 'product'),
    path('ordertracking/', views.ordertracking, name = 'ordertracking'),
    path('checkout/', views.checkout, name = 'checkout')

    
] +  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)