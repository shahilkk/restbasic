from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("addbrand", views.addbrand, name="addbrand"),
    path("editbrand/<int:id>", views.editbrand, name="editbrand"),
    path("delectdata/<int:id>", views.delectdata, name="delectdata"),
    path("profile/<int:id>", views.profile, name="profile"),
   
    path("addfeed/<int:id>", views.addfeed, name="addfeed"),
    path("viewfeed/", views.viewfeed, name="viewfeed"),
    path("getelement/<int:id>", views.getelement, name="getelement"),
    path("updatefeed/<int:id>", views.updatefeed, name="updatefeed"),
    path("test", views.test, name="test"),
   
    


]