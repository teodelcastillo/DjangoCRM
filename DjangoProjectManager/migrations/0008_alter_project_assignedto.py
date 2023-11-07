# Generated by Django 4.2.6 on 2023-11-07 00:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoProjectManager', '0007_alter_appointment_client_alter_appointment_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assignedTo',
            field=models.ManyToManyField(default=2, related_name='assigned_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
