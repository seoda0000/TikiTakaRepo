# Generated by Django 3.2.11 on 2022-11-17 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_3166_1', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('english_name', models.CharField(max_length=50)),
                ('native_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('profile_path', models.CharField(max_length=200, null=True)),
                ('name_origin', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WatchProvider',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('logo_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('adult', models.BooleanField(null=True)),
                ('video_key', models.CharField(max_length=200, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('original_title', models.CharField(max_length=100, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.CharField(max_length=200, null=True)),
                ('release_date', models.DateField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('casts', models.ManyToManyField(related_name='movies', to='movies.People')),
                ('countries', models.ManyToManyField(related_name='movies', to='movies.Country')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.people')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('watch_providers', models.ManyToManyField(related_name='movies', to='movies.WatchProvider')),
            ],
        ),
        migrations.CreateModel(
            name='Backdrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
