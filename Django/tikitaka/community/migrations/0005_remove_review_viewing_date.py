# Generated by Django 3.2.11 on 2022-11-19 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_review_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='viewing_date',
        ),
    ]