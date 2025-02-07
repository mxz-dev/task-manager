from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_tasks', 'completed_tasks']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    list_filter = ['total_tasks', 'completed_tasks']
    list_editable = ['total_tasks', 'completed_tasks']
    list_display_links = ['user']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = ['user']