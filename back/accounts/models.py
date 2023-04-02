from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    college_name = models.CharField(max_length=128, default="")
    graduation_completion = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=64, default="")
    t_shirt_size = models.CharField(max_length=3, null=True, blank=True)

    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to="media/", null=True, blank=True)
    keyword_rating = models.FloatField(null=True, blank=True)
    admin_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.username
