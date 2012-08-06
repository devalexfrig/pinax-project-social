from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    
    user = models.ForeignKey(User, related_name="profile")
    birthdate = models.DateField(null=True, blank=True)
