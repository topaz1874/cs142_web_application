from django import forms
from django.template.defaultfilters import slugify

from .models import MyUser

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = slugify(username)
        try:
            MyUser.objects.get(slug=username)
            raise forms.ValidationError("The username has been used try another.") 
        except MyUser.DoesNotExist:
            return username
        except Exception as e:
            raise e

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            MyUser.objects.get(email=email)
            raise forms.ValidationError("The email has been used try another.")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("There was an error, please try again or contact us.")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


