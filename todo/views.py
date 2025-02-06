from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import Tasks
class TasksListView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'
    paginate_by = 15
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user, completed=False).order_by('-created_at')
    
class AddTasksView(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'tasks/home.html'
    fields = ['task', 'due_time']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        messages.success(self.request, 'Task added successfully')
        return reverse('home')
    def form_invalid(self, form):
        messages.error(self.request, 'Error adding task. Please try again')
        return redirect('home')

class DeleteTasksView(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/home.html'
    def get_success_url(self):
        messages.error(self.request, 'Task deleted successfully')
        return reverse('home')

class CompleteTaskView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/home.html'
    fields = ['completed']
    context_object_name = 'task'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.completed = True
        return super().form_valid(form)
    def get_success_url(self):
        messages.success(self.request, 'Task completed successfully')
        return reverse('home')

class EditTasksView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/home.html'
    fields = ['task', 'due_time']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        messages.success(self.request, 'Task edited successfully')
        return reverse('home')
    def form_invalid(self, form):
        messages.error(self.request, 'Error editing task. Please try again')
        return redirect('home')