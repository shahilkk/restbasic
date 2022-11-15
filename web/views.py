from django.shortcuts import render
from . models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.


def home(request):
    brand=Brand.objects.all()
    market=Marketplace.objects.all()
    zipcode=Zipcode.objects.all()
    context={
        "brand":brand,
        "market":market,
        "zipcode":zipcode,

    }
    return render(request,'web/home.html',context)

def addbrand(request):
    market=Marketplace.objects.all()
    zipcode=Zipcode.objects.all()
    context={
        "market":market,
        "zipcode":zipcode
    }
    return render(request,'web/addbrand.html',context)


@csrf_exempt
def editbrand(request,id):
    editproduct=Brand.objects.get(id=id)
    data={
        "name":editproduct.name,
        "place":editproduct.place.name,
        "code":editproduct.code.zipcode,
        "created_date":editproduct.created_date,
        "image":editproduct.image.url

    }
    return JsonResponse({'brand': data})

@csrf_exempt
def delectdata(request,id):
    editproduct=Brand.objects.filter(id=id).delete()
 
    return JsonResponse({'brand': "data"})   

   

def profile(request,id):
    profile=Brand.objects.get(id=id)
    
    context={
        "profile":profile
    }
    return render(request,'web/profile.html',context)    


