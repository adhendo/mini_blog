# Generated by Django 3.0.3 on 2020-02-26 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20200226_0606'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RedditHeadlines',
            new_name='RedditHeadline',
        ),
        migrations.RenameModel(
            old_name='TwitterHeadlines',
            new_name='TwitterHeadline',
        ),
    ]
