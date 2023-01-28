from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class App(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=6)
    framework = models.CharField(max_length=6)

    domain_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
