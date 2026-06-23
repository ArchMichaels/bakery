from django.contrib import admin

from django.urls import path

from . import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path("aboutus", views.aboutus, name="aboutus"),
    path("menu", views.menu, name="menu"),
    path("home", views.home, name="home"),

]