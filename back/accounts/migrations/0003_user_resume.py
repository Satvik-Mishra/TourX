# Generated by Django 4.1.7 on 2023-04-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_address_alter_user_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to="media/resume"),
        ),
    ]
