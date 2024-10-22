# Generated by Django 4.2.16 on 2024-10-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('screen_type', models.CharField(max_length=200)),
                ('sound_system', models.CharField(max_length=200)),
                ('seating', models.PositiveIntegerField()),
            ],
        ),
    ]
