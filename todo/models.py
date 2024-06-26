from django.db import models
import datetime
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def time_passed(self):
        today = date.today()
        delta = today - self.created_at
        return delta.days
