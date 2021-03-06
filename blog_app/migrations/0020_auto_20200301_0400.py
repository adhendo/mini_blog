# Generated by Django 3.0.3 on 2020-03-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0019_youtubeheadline_youtube_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterheadline',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='twitterheadline',
            name='url',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
