# Generated by Django 3.0.3 on 2020-03-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0030_auto_20200311_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googletrends',
            name='trends',
            field=models.CharField(max_length=200000, unique=True),
        ),
    ]
