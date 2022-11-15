from django.urls import path

from . import views
from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register('addbrand', views.CreateView, basename='addbrand')
Productsrouter = routers.NestedDefaultRouter(router,'addbrand',lookup='addbrand')
urlpatterns=router.urls +Productsrouter.urls



router.register('editdatas', views.UpdateView, basename='editdatas')
editsrouter = routers.NestedDefaultRouter(router,'editdatas',lookup='editdatas')
urlpatterns=router.urls +editsrouter.urls
# urlpatterns = [
#     path('addbrand',views.CreateView.as_view()),
#     path('editdatas/<int:pk>',views.UpdateView.as_view()),
# ] 