from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('profile_search', views.profile_search, name= 'profile_search'),
    path('locations', views.location_getter, name= 'locations'),
    path('scrape/', views.scrape, name="scrape"),
]