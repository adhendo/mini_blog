# Generated by Django 3.0.3 on 2020-03-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0021_auto_20200301_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditheadline',
            name='reddit_title',
            field=models.CharField(max_length=2000, unique=True),
        ),
        migrations.AlterField(
            model_name='youtubeheadline',
            name='youtube_title',
            field=models.CharField(max_length=2000, unique=True),
        ),
    ]