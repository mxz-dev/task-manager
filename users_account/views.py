from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['avatar']
    template_name = 'account/profile_update.html'
    def get_success_url(self):
        messages.success(self.request, 'Profile updated successfully')
        return reverse('profile', kwargs={'username': self.request.user.username})
