# Generated by Django 3.0.3 on 2020-02-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20200226_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redditheadline',
            name='id',
        ),
        migrations.RemoveField(
            model_name='twitterheadline',
            name='id',
        ),
        migrations.AlterField(
            model_name='redditheadline',
            name='reddit_title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='twitterheadline',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
