from django.shortcuts import render, redirect
from . models import Product
from . forms import ProductForm


# Create your views here.


def ShowAllProducts(request):
    products = Product.objects.all()
    
    context = {
        'products' : products
    }
    
    return render(request, 'showProduct.html', context)


def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)
    
    context = {
        'eachProduct' : eachProduct
    }

    return render(request, 'productDetail.html', context) 


def addProduct(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
        else:
            form = ProductForm()
    
    context = {
        'form':form
    }
    return render(request, 'addProduct.html',context)


def updateProduct(request,pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        "form":form
    }

    return render(request, 'updateProduct.html', context)



def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')