from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)