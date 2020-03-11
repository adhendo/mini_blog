from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Searches'

class TwitterHeadline(models.Model):
  title = models.CharField(unique=True, max_length=2000)
  image = models.URLField(null=True, blank=True)
  url = models.TextField(primary_key=True)
  tag = models.CharField(null=True, blank=True, max_length=2000)
  time = models.CharField(null=True, blank=True, max_length=2000)
  likes = models.ManyToManyField(User, related_name='likesTwitter', blank=True)
  created = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title

class RedditHeadline(models.Model):
  reddit_title = models.CharField(unique=True, max_length=2000)
  reddit_image = models.URLField(null=True, blank=True)
  reddit_url = models.TextField(primary_key=True)
  reddit_thumbnailUrl = models.URLField(null=True, blank=True)
  reddit_tag =  models.TextField(null=True, blank=True)
  reddit_time = models.TextField(null=True, blank=True)
  likes = models.ManyToManyField(User, related_name='likesReddit', blank=True)
  created = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.reddit_title

class YoutubeHeadline(models.Model):
    youtube_title = models.CharField(unique=True, max_length=2000)
    youtube_url = models.TextField(primary_key=True)
    youtube_image = models.URLField(null=True, blank=True)
    youtube_info = models.TextField(null=True, blank=True)
    youtube_thumbnailUrl = models.URLField(null=True, blank=True)
    youtube_metadata = models.TextField(null=True, blank=True)
    youtube_channel = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likesYoutube', blank=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.youtube_title

class GoogleTrends(models.Model):
    trends = models.CharField(max_length=200000)
    realtimetrends = models.CharField(null=True, blank=True,max_length=200000)
    created = models.DateTimeField(auto_now=True)
