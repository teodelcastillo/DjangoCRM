# Generated by Django 4.2.6 on 2023-11-06 23:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoProjectManager', '0003_appointment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='assignedTo',
            field=models.ManyToManyField(default=2, related_name='assigned_clients', to=settings.AUTH_USER_MODEL),
        ),
    ]