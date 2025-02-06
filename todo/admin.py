from django.contrib import admin
from .models import Tasks
# Register your models here.


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user','task', 'due_time', 'completed', 'created_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('task', 'due_time')
    ordering = ('-created_at',)