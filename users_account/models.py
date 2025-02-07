from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', default="avatars/default.png", null=True, blank=True)
    total_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} profile'
