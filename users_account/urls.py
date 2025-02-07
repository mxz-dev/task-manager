from django.urls import path
from . import views
urlpatterns = [
    path('profile/<slug:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/update', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('user-info/update', views.UserInfoUpdateView.as_view(), name='user_update'),
]
