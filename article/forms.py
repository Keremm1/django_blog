from django import forms
#https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]
