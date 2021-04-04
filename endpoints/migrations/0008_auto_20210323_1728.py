# Generated by Django 3.1.7 on 2021-03-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0007_auto_20210319_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='type',
            field=models.CharField(choices=[('song', 'Song'), ('podcast', 'Podcast'), ('audiobook', 'Audiobook')], max_length=10),
        ),
    ]
