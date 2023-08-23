from django.db import models


class TimedStamped(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class META:
		abstract = True
