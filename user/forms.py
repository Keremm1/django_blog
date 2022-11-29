from django import forms


#https://docs.djangoproject.com/en/4.1/ref/forms/api/
#https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
#https://docs.djangoproject.com/en/4.1/ref/validators/
#https://github.com/django-ckeditor/django-ckeditor?ysclid=lao1f1bwz8711310387

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)
    


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "Kullanıcı Adı",widget=forms.Textarea)
    password = forms.CharField(max_length=20,label="Parola",widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget= forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor...")
        values = {
            "username" : username,
            "password" : password
        }
        return values
        

    
    #https://docs.djangoproject.com/en/4.1/topics/forms/


