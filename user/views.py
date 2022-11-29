from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from random import randint
from django.contrib.auth import login,authenticate,logout
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
# Create your views here.

from random import randint
letters = "0123456789ABCDEF"
color= "#"
data = User.objects.all()
a=0
while a <= len(data)-1:
    for i in range(0,6):
        k = randint(0,15)
        color +=letters[k]
    data[a].last_name = color
    data[a].save()
    a +=1
    color = ""
    

def register(request):
    
    form = RegisterForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.get_or_create(username=username)
            if user[1]:
                user[0].set_password(password)
                letters = "0123456789ABCDEF"
                color= "#"
                for i in range(0,6):
                    k = randint(0,15)
                    color +=letters[k]
                user[0].last_name = color
                user[0].save()
                messages.info(request,"***You have successfully registered***")
                return redirect("user:login")
            else:
                messages.info(request,"Kullanıcı adı kullanımda başka bir kullanıcı adı takmayı deneyin...")
                return render(request,"register.html",context) 
            
            
    
    return render(request,"register.html",context) 
    """
    if request.method ==  "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)

            return redirect("index")
    context = {
        "form":form
    }
    return render(request,"register.html",context)
    """
def loginn(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user == User.objects.get(username=username):
            messages.success(request,"Giriş Başarılı...")
            login(request,user)
            return redirect("index")
        elif user is None:
            messages.info(request,"Kullanıcı adı veyaparola hatalı..")
            return render(request,"login.html",context) 
    return render(request,"login.html",context) 
    

    
def logoutt(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız...")
    return redirect("index")

class user_page(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = "user:login"
    template_name = "user_page.html"
    def get(self,request,id):
        info = User.objects.filter(id=id)
        if info:
            is_self = 1
            if request.user.id == id: return render(request,self.template_name,{"info":info,"is_self":is_self})
            return render(request,self.template_name,{"info":info}) 
        messages.error("Böyle bir kullanıcı yok.")
        return redirect("user:login")
    def post(self,request,id):
        pass