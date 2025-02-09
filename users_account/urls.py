from django.urls import path
from . import views
urlpatterns = [
    path('profile/<slug:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/<slug:username>/', views.UserProfileUpdateView.as_view(), name='profile_update'),
    path('user-info/update/<slug:username>/', views.UserInfoUpdateView.as_view(), name='user_update'),
]
