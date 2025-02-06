from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=150)
    due_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
    class Meta:
        verbose_name_plural = 'Tasks'