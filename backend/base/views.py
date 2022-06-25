from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html',{})
class ProductList(View):
    def get(self,request):
        #récuperer depuis bdd
        produits=Product.objects.all()
        return render(request,'listProducts.html',{'prod':produits})
class ProductDetails(View):
    def get(self,request,idprod):
        produit=Product.objects.get(id=idprod)
        return render(request,'details.html',{'prod':produit})
class ProductBasket(View):
    def get(self,request,idpanier):
        produit=Product.objects.get(id=idpanier)
        return render(request,'Basket.html',{'prod':produit})

