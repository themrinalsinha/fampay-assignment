from django.urls import path
from .views import yt_feed_list

urlpatterns = [
    path('list/', yt_feed_list, name='yt_feed_list'),
]
