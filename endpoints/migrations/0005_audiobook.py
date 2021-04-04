# Generated by Django 3.1.7 on 2021-03-16 19:22

from django.db import migrations, models
import django_seconds_field


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0004_podcast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True, help_text='audio uploaded time')),
                ('duration', django_seconds_field.SecondsField(help_text='audio duration')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
