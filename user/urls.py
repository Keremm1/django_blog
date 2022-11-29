from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"


urlpatterns=[
    path("register/",views.register,name="register"),
    path("login/",views.loginn,name="login"),
    path("logout/",views.logoutt,name="logout"),
    path("userpage/<int:id>",views.user_page.as_view(),name="user_page")

]