from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("addbrand", views.addbrand, name="addbrand"),
    path("editbrand/<int:id>", views.editbrand, name="editbrand"),
    path("delectdata/<int:id>", views.delectdata, name="delectdata"),
    path("profile/<int:id>", views.profile, name="profile"),
    # path('countries/<str:pk>/', login_required(views.CountryDetailView.as_view()),name='country_detail'),
   
    


]