from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fitness_level = models.CharField(max_length=50)
    running_goals = models.TextField()

    def __str__(self):
        return self.user.username
    