# Generated by Django 3.0.3 on 2020-03-11 01:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0023_savedarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditheadline',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likesReddit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='twitterheadline',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likesTwitter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='youtubeheadline',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likesYoutube', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='SavedArticle',
        ),
    ]
