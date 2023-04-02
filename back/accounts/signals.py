from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from django.dispatch import receiver

from PyPDF2 import PdfReader

from accounts.models import User


@receiver(post_save, sender=User)
def update_keyword_rate(sender, instance, created, **kwargs):
    user = instance
    resume = user.resume
    if resume:
        reader = PdfReader(resume)
        page = reader.pages[0]
        text = page.extract_text()

