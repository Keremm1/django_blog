"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from article import views
from django.conf.urls import handler404,handler403,handler500
from article import views 
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),  
    path("about/",views.about,name="about"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("articles/",include("article.urls")),
    path("user/",include("user.urls")),
    path("api/",include("article.api.urls")),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
handler403 = views.error_403
handler404 = views.error_404
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
