# Generated by Django 3.2.11 on 2022-11-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='start',
            field=models.CharField(max_length=300),
        ),
    ]