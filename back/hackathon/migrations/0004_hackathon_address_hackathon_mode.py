# Generated by Django 4.1.7 on 2023-04-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hackathon", "0003_hackathon_teams_team_code_team_member"),
    ]

    operations = [
        migrations.AddField(
            model_name="hackathon",
            name="address",
            field=models.CharField(default="", max_length=128),
        ),
        migrations.AddField(
            model_name="hackathon",
            name="mode",
            field=models.CharField(
                blank=True,
                choices=[("online", "Online"), ("offline", "Offline")],
                default="offline",
                max_length=32,
                null=True,
            ),
        ),
    ]
