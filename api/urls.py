from django.urls import path

from . import views
from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('brands', views.CreateView, basename='brands')

brand_router = routers.NestedDefaultRouter(router, 'brands', lookup='brand')
brand_router.register('feed', views.FeedViewSet,basename='brand-feed')

urlpatterns=router.urls + brand_router.urls    