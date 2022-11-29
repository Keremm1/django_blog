from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
#https://ceakssan.com/tr/middleware-nedir-ne-ise-yarar
#https://docs.djangoproject.com/en/4.1/topics/http/middleware/
#https://docs.djangoproject.com/en/4.1/ref/models/options/
class Article(models.Model):
                               #"auth.user"
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Yazar",related_name="articles") #başka bir tabloyu göstermek istiyorsak Foreign key i kullanmamız gerekiyor,yani burada yazar tablomuzu django'dan hazır user tablosunu çekiyoruz 
                                                            #on_delete'nin anlamı ise user silindiğinde makalenin de silinmesi anlamını veriyor
    
    title = models.CharField(max_length=50,verbose_name="Başlık")
    #content = models.TextField(verbose_name="İçerik")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi") #o anki tarihi direkt olarak atar
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title
    class Meta:
        ordering =["-created_date"]
    #def clean()
class Hashtags(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    linked_article = models.ForeignKey("article.article",on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="isim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =["-comment_date"]