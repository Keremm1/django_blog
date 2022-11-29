from django.contrib import admin
from django.urls import path,re_path
from . import views
app_name="article"

urlpatterns=[
    path("dashboard/",views.dashboard,name="dashboard"),
    path("createarticle/",views.createarticle,name="createarticle"),
    path("article/<int:id>",views.article.as_view(),name="article"),
    path("update/<int:id>",views.update.as_view(),name="update"),
    path("delete/<int:id>",views.deleteArticle,name="delete"),
    path("",views.articles,name="articles"),
    re_path(r'^update/(?P<id>\d+)/$', views.update.as_view())
    
]

