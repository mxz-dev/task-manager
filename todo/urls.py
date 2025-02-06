from django.urls import path
from . import views
urlpatterns = [
    path('', views.TasksListView.as_view(), name='home'),
    path('add-task', views.AddTasksView.as_view(), name='add_task'),
    path('delete-task/<int:pk>', views.DeleteTasksView.as_view(), name='delete_task'),
]
