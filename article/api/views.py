from  rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#class views
from rest_framework.views import APIView

from rest_framework.generics import get_object_or_404

from article.models import Article
from article.api.serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User
#CLASS BASED VİEWS

from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username" #users/lookup_field

class UserListCreateAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many = True,context={'request':request})#context={'request':request} ekleme sebebimiz ise HyperLinked ekleme anlamı
        return Response(serializer.data)
    
    def post(self,request):
        user = UserSerializer(data =request.data)
        if user.is_valid():
            user.save()
            return Response(user.data,status=status.HTTP_201_CREATED)
        return  Response(user.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleListCreateAPIView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        article = ArticleSerializer(data =request.data)
        if article.is_valid():
            article.save()
            return Response(article.data,status=status.HTTP_201_CREATED)
        return  Response(article.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    def get_object(self,id):
        article_instance = get_object_or_404(Article,id=id)
        return article_instance
    def get(self,request,id):
        article =self.get_object(id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def put(self,request,id):
        article =self.get_object(id=id)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        article =self.get_object(id=id)
        article.delete()  
        return Response(
            {
                "errors": {
                    'code':204,
                    "message": f'{id} adlı numaralı makale silinmiştir'
                } 
            },

            status=status.HTTP_204_NO_CONTENT
        )





#FUNCTİON BASED VİEWS
# @api_view(["GET","POST"])
# def article_list_create_api_view(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many = True)
#         return Response(serializer.data)
#     else:
#         article = ArticleSerializer(data =request.data)
#         if article.is_valid():
#             article.save()
#             return Response(article.data,status=status.HTTP_201_CREATED)
#         return  Response(status=status.HTTP_400_BAD_REQUEST)
# @api_view(["GET","PUT","DELETE"])
# def article_detail_api_view(request,id):
#     try:
#         article_instance = Article.objects.get(id=id)
#     except Article.DoesNotExist:
#         return Response(
#             {
#                 "errors": {
#                     'code':404,
#                     "message": f'Böyle bir id {id} ile ilgili makale bulunamadı.'
#                 } 
#             },

#             status=status.HTTP_404_NOT_FOUND
#         )
#     if request.method == "GET":
#         serializer = ArticleSerializer(article_instance)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article_instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)  
#     elif request.method == "DELETE": #json da True değil true 
#         article_instance.delete()        #json formatına api/makaleler den bakabiliriz
#         return Response(
#             {
#                 "errors": {
#                     'code':204,
#                     "message": f'{id} adlı numaralı makale silinmiştir'
#                 } 
#             },

#             status=status.HTTP_204_NO_CONTENT
#         )

