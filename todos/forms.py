from django import forms
from .models import todo, login, register
from django.contrib.auth.models import User


class TodosForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'description', 'till', 'done']
        widgets = {
            'till': forms.DateInput(attrs={'type': 'date'})
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['login', 'password']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = register
        fields = ['first_name', 'last_name', 'username', 'password', 'password2', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email is not unique")
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username is not unique")
        else:
            return username

    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The two password fields didn't match.")
        return password2
