from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth import get_user_model
from django import forms
from captcha.fields import CaptchaField
from .models import Profile
User = get_user_model()
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    captcha = CaptchaField(label='Are you human?', )

class CustomLoginForm(LoginForm):
    captcha = CaptchaField(label='Are you human?', )
    