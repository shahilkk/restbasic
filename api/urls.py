from django.urls import path

from . import views
from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('brand', views.CreateView, basename='brand')

brand_router = routers.NestedDefaultRouter(router, 'brand', lookup='brand')
urlpatterns=router.urls + brand_router.urls    