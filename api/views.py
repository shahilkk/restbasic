from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from . import serializers
from web.models import Brand
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import viewsets
# Creae your views here.

class CreateView(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = serializers.CreateUser
    def get_queryset(self):
        return Brand.objects.all()
    
    
    
class UpdateView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers.EditSerializer
    permission_classes = (AllowAny,)
    # costomize delect with another query
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_serializer_context(self):
        return {"request": self.request}