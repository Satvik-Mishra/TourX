import base64
import uuid
from django.db import models
from accounts.models import User


def generate_short_uuid():
    short_uuid = format(uuid.uuid4().int & (1 << 24) - 1, "06x")
    return short_uuid


class Team(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=6, default=generate_short_uuid)
    member = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.name


class Hackathon(models.Model):
    hackathon_mode = [
        ("online", "Online"),
        ("offline", "Offline"),
    ]
    name = models.CharField(max_length=64)
    description = models.TextField()
    logo = models.ImageField(upload_to="media", null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_members = models.IntegerField()
    min_members = models.IntegerField()
    address = models.CharField(max_length=128, default="")
    mode = models.CharField(
        max_length=32,
        choices=hackathon_mode,
        default=hackathon_mode[1][0],
        null=True,
        blank=True,
    )
    teams = models.ManyToManyField(Team, null=True, blank=True, default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default=None
    )

    @property
    def team_count(self):
        return self.teams.count()

    def __str__(self):
        return self.name
