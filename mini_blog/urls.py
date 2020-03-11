"""mini_blog URL Configuration"""

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('blog_app.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

]
