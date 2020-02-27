from rest_framework import serializers
from .models import TwitterHeadline, RedditHeadline, YoutubeHeadline

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeHeadline
        fields = ('youtube_title', 'youtube_url', 'youtube_image', 'youtube_info')

class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterHeadline
        fields = ('title', 'image', 'url', 'tag', 'time')

class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditHeadline
        fields = ('reddit_title', 'reddit_image', 'reddit_url', 'reddit_tag', 'reddit_time')

