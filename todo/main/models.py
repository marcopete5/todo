from __future__ import unicode_literals

from django.db import models

class List(models.Model):
	task = models.CharField(max_length=70)
	date = models.DateField(null=True, blank=True)
	done = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='List'

	def __unicode__(self):
		return self.task




