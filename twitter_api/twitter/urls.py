from django.urls import path
from twitter.views import TweetView

urlpatterns = [
    path('api', TweetView.as_view()),
]
