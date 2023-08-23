from django.urls import path, include

urlpatterns = [
    path('twitter/', include("twitter.urls"))
]
