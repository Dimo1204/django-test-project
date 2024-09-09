from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Product
from .forms import AddProductForm

# Create your views here.
def index(request: HttpRequest):
    products = Product.objects.all()
    print("Товары", products)
    return render(request, "index.html", {"products" : products})


def add_product(request: HttpRequest):
    if request.method == "GET":
        form = AddProductForm()
        return render(request, "add_product.html", {"form" : form}) # контекст для шаблона
    elif request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = Product(**data)
            product.save()
            return redirect("index")
        else:
            return render(request, "add_product.html", {"form" : form})