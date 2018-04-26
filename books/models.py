# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Books(models.Model):
	title = models.CharField(max_length=150, blank=False)
	author = models.CharField(max_length=70, blank=False)
	review = models.TextField(max_length=500, blank=True, null=True)
	date_reviewed = models.DateTimeField(default=None, blank=True, null=True)
	is_favourite = models.BooleanField(default=False, verbose_name="Favourite")

	def __unicode__(self):
		return self.title + " " + self.author

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"

