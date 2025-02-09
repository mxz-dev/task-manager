from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib import messages
from .models import Profile
from todo.models import Tasks
from django.contrib.auth import get_user_model


User = get_user_model()
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    def get_object(self):
        profile = Profile.objects.get(user__username=self.kwargs['username'])
        profile.total_tasks = Tasks.objects.filter(user__username=self.kwargs['username']).count()
        profile.completed_tasks = Tasks.objects.filter(user__username=self.kwargs['username'], completed=True).count()

        return profile
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['avatar']
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Profile updated successfully')
        return reverse('profile', kwargs={'username': self.request.user.username})
class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'account/user_info_update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        messages.success(self.request, 'User info updated successfully')
        return reverse('profile', kwargs={'username': self.request.user.username})
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        if User.objects.filter(username=username).exists() and username != self.request.user.username:
            messages.error(self.request, 'Username already exists')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    