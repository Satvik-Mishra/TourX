import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from hackathon.models import Team


def generate_short_uuid():
    short_uuid = format(uuid.uuid4().int & (1 << 24) - 1, "06x")
    return short_uuid


@receiver(post_save, sender=Team)
def generate_team_uuid(sender, instance, created, **kwargs):
    if created:
        code = generate_short_uuid()
        instance.code = code
        instance.save()
