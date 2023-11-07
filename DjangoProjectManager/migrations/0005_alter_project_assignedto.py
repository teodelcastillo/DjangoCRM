# Generated by Django 4.2.6 on 2023-11-06 23:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoProjectManager', '0004_client_assignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assignedTo',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]