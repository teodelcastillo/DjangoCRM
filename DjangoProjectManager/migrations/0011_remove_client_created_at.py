# Generated by Django 4.2.6 on 2023-11-08 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoProjectManager', '0010_alter_client_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_at',
        ),
    ]
