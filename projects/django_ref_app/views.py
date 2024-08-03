from django.shortcuts import HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import Customer, Products
import json


def index(request):
    customer_set = Customer.objects.all()
    customers = []
    for client in customer_set:
        customers.append({
            'name': client.name,
            'location': client.location
        })
    pdt_set = Products.objects.all()
    products = []
    for pdt in pdt_set:
        products.append({
            'name': pdt.pdt_name,
            'cost': pdt.cost,
            'quantity': pdt.quantity
        })
    print(request.COOKIES)
    return JsonResponse([customers, products], safe=False)

@csrf_exempt
def add_customer(request):
    # get customer data as post dict
    name = request.POST['name']
    location = request.POST['location']
    c1 = Customer(name=name, location=location)
    c1.save()
    return HttpResponse('Added Customer', status=200)


@csrf_exempt
def add_product(request):
    name = request.POST['name']
    cost = float(request.POST['cost'])
    quantity= int(request.POST['qty'])
    p1 = Products(pdt_name=name, cost=cost, quantity=quantity)
    p1.save()
    return HttpResponse('Product added')


@csrf_exempt
def update_product(request, pk):
    """Update product has to be PUT request
    as the product already exists."""
    if request.method == 'PUT':
        # get the object from the database
        p1 = get_object_or_404(Products, pk=pk)
        # print(p1)
        # update the data in the object
        print(request.body.decode("utf-8"))
        data = json.loads(request.body.decode('utf-8'))
        p1.pdt_name = data['name']
        p1.cost = data['cost']
        p1.quantity = data['qty']
        # upsert the data to database
        p1.save()
        # return success response
        return HttpResponse(status=200)
    # print(request.body)
    # print(request.COOKIES)
    # print(type(request))
    # print(request.method)
    # print(request.scheme)
    # print(request.path)
    # print(request.encoding)
    # print(request.content_type)
    # print(request.content_params)
    # print(request.POST)
    # print(request.GET)
    return HttpResponse(status=404)

@csrf_exempt
def delete_product(request, pk):
    """Deletes the product from the
    database."""
    if request.method == 'DELETE':
        Products.objects.filter(pk=pk).delete()
        return HttpResponse(status=204)

    return HttpResponse(status=404)

@csrf_exempt
def patch_product(request, pk):
    """updates the product partially"""
    print(request.body.decode("utf-8"))
    print(request.method)
    if request.method == 'PATCH':
        p1 = get_object_or_404(Products, pk=pk)
        data = json.loads(request.body.decode('utf-8'))
        if 'name' in data:
            p1.pdt_name = data['name']
        if 'qty' in data:
            p1.quantity = data['qty']
        if 'cost' in data:
            p1.cost = data['cost']
        p1.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)
