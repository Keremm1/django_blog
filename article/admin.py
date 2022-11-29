from django.contrib import admin #contrib settingsteki Instakk--lled appsteki stringleri hatırlatsın

#
from .models import Article,Hashtags,Comment

#

# Register your models here.
#https://docs.djangoproject.com/en/2.0/ref/contrib/admin/
#https://docs.djangoproject.com/en/4.1/topics/db/queries/
admin.site.register(Hashtags)
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):#admin.site.register(Article)
    list_display = ["title","author","created_date"]
    list_display_links = ["title","author"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article