from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742636 Punyanuch Pocharapongpan views!')

def item_view(request, item_id):

    context_data = {
        "item_id": item_id
    }

    return render(request, 'index.html',context = context_data)

def home_view(req):
    return render(req, 'homepage.html')

def category_view(req):
    return render(req, 'category.html')

def product_view(req):
    return render(req, 'product.html')

def checkout_view(req):
    return render(req, 'checkout.html')

def contact_view(req):
    return render(req, 'contact.html')