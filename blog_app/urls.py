from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', views.news_list, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('profile_search', views.profile_search, name= 'profile_search'),
    path('scrape/', views.scrape, name="scrape"),
    path('scrapeReddit/', views.scrapeReddit, name="scrapeReddit"),
    path('scrapeYoutube/', views.scrapeYoutube, name="scrapeYoutube"),
    path('scrapeTwitter/', views.scrapeTwitter, name="scrapeTwitter"),
    path('scrapeGoogle/', views.scrapeGoogle, name="scrapeGoogle"),
    #path(r'^like/$', views.like_post, name="like_post")
]