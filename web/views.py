from django.shortcuts import render,redirect
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
 
    return redirect('/')

   

def profile(request,id):
    profile=Brand.objects.get(id=id)
    
    context={
        "profile":profile
    }
    return render(request,'web/profile.html',context)    

def addfeed(request,id):
    
    context={
        "id":id
    }
    return render(request,'web/addfeed.html',context)    

def viewfeed(request):
    
    context={
    }
    return render(request,'web/viewfeed.html',context)    


@csrf_exempt
def getelement(request,id):
    brand=Brand.objects.get(id=id)
    feeds=Feed.objects.filter(brand=brand)
    data = []

    for feed in feeds:
        feeditem = {
            "feedid" : feed.id,
            "subject" : feed.subject,
            "sprit_category" : feed.sprit_category,
            "sprit_subcategory" : feed.sprit_subcategory,
            "wine_category" : feed.wine_category,
            "wine_subcategory": feed.wine_subcategory,
            "beer_category" : feed.beer_category,
            "beer_subcategory" : feed.beer_subcategory,
            "name" : feed.brand.name,
            "image" : feed.brand.image.url,
            "place" : feed.brand.place.logo.url,
        }
        data.append(feeditem)
    return JsonResponse({'data':data,})

def updatefeed(request,id):
    feed=Feed.objects.get(id=id)
    context={
        "feed":feed
    }
    return render(request,'web/updatefeed.html',context)    