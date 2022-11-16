from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from .serializers import CreateUser,EditSerializer,FeedSerializer
from web.models import Brand,Feed
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import viewsets
# Creae your views here.

class CreateView(ModelViewSet):
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return Brand.objects.all()
    http_method_names = ['get', 'post', 'put','patch', 'delete']    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CreateUser
        elif self.request.method == 'POST':
            return EditSerializer
        elif self.request.method == 'PATCH':
            return EditSerializer    
        elif self.request.method == 'PUT':
            return EditSerializer    
        return CreateUser
    
    
class FeedViewSet(ModelViewSet):
    serializer_class = FeedSerializer

    def get_queryset(self):
        return Feed.objects.filter(brand_id=self.kwargs['brand_pk'])

    def get_serializer_context(self):
        return {'brand_id': self.kwargs['brand_pk']}   