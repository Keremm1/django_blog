from django.urls import path
from article.api import views as api_views

#http://www.django-rest-framework.org/api-guide/routers/

# from rest_framework.routers import DefaultRouter

# from article.api.views import UserViewSet
# app_name = "blog"
# router = DefaultRouter()
# router.register("users", UserViewSet)
#CLASS BASED VİEWS
urlpatterns = [
    path("makaleler/",api_views.ArticleListCreateAPIView.as_view(),name="api-listesi"),
    path("makaleler/<int:id>",api_views.ArticleDetailAPIView.as_view(),name="api-articles"),
    path("users/",api_views.UserListCreateAPIView.as_view(),name="user-list")
]   


#FUNCTİON BASED VİEWS
# urlpatterns = [
#     path("/makaleler",api_views.article_list_create_api_view,name="makale-listesi"),
#     path("/makaleler/<int:id>",api_views.article_detail_api_view,name="makale_detay")

# ]