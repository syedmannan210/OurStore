from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil

# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    # nslides=(n//4)+ceil((n/4) - (n//4))
    # params={'no_of_slides': nslides, 'product':products,range:nslides}
    # allProds=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    # params={'allProds':allProds}
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}#set comprehension to iterate over the categories of the products.
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nslides), nslides])

    params = {'allProds': allProds}
    return render(request,"shop/index.html", params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        contact_desc=request.POST.get('contact_desc','')
        # print(name,email,phone,contact_desc)
        contact=Contact(name=name,email=email,phone=phone,contact_desc=contact_desc)
        contact.save()
    return render(request, 'shop/contact.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def productView(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/ProdView.html',{'product': product[0]})
def search(request):
    return render(request, 'shop/search.html')
def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})

    return render(request, 'shop/checkout.html')