from django.shortcuts import render

# Create your views here.
def products(request):
    return render(request, 'products/products.html', {
        "title" : "Products",
        "items" : ["Shirts", "Pants", "Shoes"]
    })