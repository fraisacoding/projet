from django.urls import path
from .views import Home
from .views import ProductList
from . import views
from django.conf.urls.static import static
from django.conf import settings
from.views import *
urlpatterns=[
    path('',views.Home.as_view(),name='Home'),
    path('products/',views.ProductList.as_view(),name='products'),
    path('products/<int:idprod>',ProductDetails.as_view(),name='products_details'),
    path('products/<int:idpanier>',views.ProductBasket.as_view(),name='Add_product'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)