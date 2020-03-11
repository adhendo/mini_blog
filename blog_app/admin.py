from django.contrib import admin
from .models import Search, TwitterHeadline, RedditHeadline, YoutubeHeadline, GoogleTrends


# Register your models here.
admin.site.register(Search)
admin.site.register(TwitterHeadline)
admin.site.register(RedditHeadline)
admin.site.register(YoutubeHeadline)
admin.site.register(GoogleTrends)