from twitter.utils import TimedStamped
from django.db import models


class Tweet(TimedStamped):
	message = models.CharField(max_length=50)
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ["-id"]
