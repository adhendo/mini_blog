# Generated by Django 3.0.3 on 2020-03-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0032_auto_20200311_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='googletrends',
            name='realtimetrends',
            field=models.CharField(blank=True, max_length=200000, null=True),
        ),
    ]
