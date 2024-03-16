from django.shortcuts import render
from .models import Category,Product

# Create your views here.
def myhome(request):
    categories = Category.get_all_categories()
    products = Product.get_all_products()
    mydict = {}
    print(products)
    mydict['category_items']=categories
    mydict['product_items']=products
    return render(request,"home.html",mydict)

def contact(request):
    return render(request,"contact.html")
def shop(request):
    return render(request,"shop.html")

def form(request):
    if request.method=='GET':
        print("Get Method Called")
    elif request.method=='Post':
        print("Post Method Called")
    return render(request,"form.html")

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def testimonial(request):
    return render(request,"testimonial.html")