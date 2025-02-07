from django.urls import path
from . import views
urlpatterns = [
    path('', views.TasksListView.as_view(), name='home'),
    # CRUD operations for tasks
    path('add-task', views.AddTasksView.as_view(), name='add_task'),
    path('delete-task/<int:pk>', views.DeleteTasksView.as_view(), name='delete_task'),
    path('complete-task/<int:pk>', views.CompleteTaskView.as_view(), name='complete_task'),
    path("edit-task/<int:pk>", views.EditTasksView.as_view(), name='edit_task'),
    path("incomplete-tasks/<int:pk>", views.IncompleteTasksView.as_view(), name='incomplete_task'),
    
    # completed tasks
    path('completed-tasks', views.CompletedTasksView.as_view(), name='completed_tasks'),
]
