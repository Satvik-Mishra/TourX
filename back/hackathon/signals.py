import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver

from hackathon.models import Team


def generate_short_uuid():
    return str(uuid.uuid4().int & (1 << 24) - 1)


@receiver(pre_save, sender=Team)
def generate_team_uuid(sender, instance, **kwargs):
    if not instance.uuid:
        instance.uuid = generate_short_uuid()
