# Generated by Django 3.2.11 on 2022-11-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_img',
        ),
    ]