# Generated by Django 3.0.3 on 2020-03-10 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0022_auto_20200301_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reddit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog_app.RedditHeadline')),
                ('twitter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog_app.TwitterHeadline')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('youtube', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog_app.YoutubeHeadline')),
            ],
        ),
    ]
