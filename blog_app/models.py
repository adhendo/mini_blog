from django.db import models

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
  created = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title

class RedditHeadline(models.Model):
  reddit_title = models.CharField(unique=True, max_length=200)
  reddit_image = models.URLField(null=True, blank=True)
  reddit_url = models.TextField(primary_key=True)
  reddit_tag =  models.TextField(null=True, blank=True)
  reddit_time = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.reddit_title

class YoutubeHeadline(models.Model):
    youtube_title = models.CharField(unique=True, max_length=200)
    youtube_url = models.TextField(primary_key=True)
    youtube_image = models.URLField(null=True, blank=True)
    youtube_info = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.youtube_title