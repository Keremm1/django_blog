from functools import wraps
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from  django.views import View
# Create your views here.
#https://startbootstrap.com/template/blog-post
#https://docs.djangoproject.com/en/4.1/topics/auth/
#https://docs.djangoproject.com/en/4.1/topics/http/middleware/

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def detail(request,id): 
    return HttpResponse("Detail"+ str(id))

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)  
    context = {"articles":articles}


    return render(request,"dashboard.html",context)


@login_required(login_url="user:login")
def createarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu...")
        return redirect("article:dashboard") 
    return render(request,"createarticle.html",{"form":form})



class article(View):
    template_name = "article.html"
    login_url = '/user/login/'
    def get(self,request,id):
        articlee = get_object_or_404(Article,id=id)
        comments = articlee.comments.all()
        return render(request,"article.html",{"article":articlee,"comments":comments})
    def post(self,request,id):
        comment = request.POST.get("comment")
        articlee = get_object_or_404(Article,id=id)
        if comment:Comment.objects.create(article = articlee,comment_author = request.user,comment_content=comment)
        comments = articlee.comments.all()
        return render(request,"article.html",{"article":articlee,"comments":comments})


class update(LoginRequiredMixin,UserPassesTestMixin, View):
    form_class = ArticleForm
    template_name = "update.html"
    login_url = '/user/login/'
    redirect_field_name = '/articles/update/<int:id>'
    def get(self,request,id):
        article = get_object_or_404(Article,id=id)
        self.id = id
        form = self.form_class(instance=article)
        return render(request,self.template_name,{"form":form})
    def post(self,request,id):
        article = get_object_or_404(Article,id=id)
        form = self.form_class(request.POST or None,request.FILES or None,instance=article)
        if form.is_valid():
            article = form.save(commit= False)
            article.author = request.user
            article.save()
            messages.success(request,"Makeleniz Güncellendi...")
            return redirect("article:dashboard")
        return render(request,self.template_name,{"form":form})
    def test_func(self):
        article = get_object_or_404(Article,id=self.kwargs["id"])
        return self.request.user == article.author

    
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale başarıyla silindi!!!")
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def error_404(request,exception):
    return render(request,'error_404.html',status=404)

def error_403(request,exception):
    return render(request,'error_403.html',status=403)

    




