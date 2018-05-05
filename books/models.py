#- *- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Books(models.Model):
	GENRE_FICTION = 'FICTION'
	GENRE_NON_FICTION = 'NON_FICTION'
	GENRE_SELF_HELP = 'SELF_HELP'
	GENRE_THRILLER = 'THRILLER'
	GENRE_HORROR = 'HORROR'
	GENRE_EROTICA = 'EROTICA'

	genre_choices = (
		(GENRE_FICTION, 'fiction'),
		(GENRE_NON_FICTION, 'non_fiction'),
		(GENRE_HORROR, 'horror'),
		(GENRE_EROTICA, 'erotica'),
		(GENRE_SELF_HELP, 'self_help'))

	title = models.CharField(max_length=150, blank=False)
	genre = models.CharField(max_length=30, blank=False, default=GENRE_FICTION, choices=genre_choices)
	date_reviewed = models.DateTimeField(default=None, blank=True, null=True)
	is_favourite = models.BooleanField(default=False, verbose_name="Favourite")
	authors = models.ManyToManyField("Author")
	review = models.ForeignKey("Review", null=True)

	def __unicode__(self):
		return self.title + " " + self.author

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"


class Author(models.Model):
	first_name = models.CharField(max_length=20, blank=False, null=False)
	last_name = models.CharField(max_length=20, blank=True, null=True)
	age = models.IntegerField(blank=True, null=True, default=30)
	sex = models.CharField(max_length=10, blank=True, null=True)
	experience = models.FloatField(blank=True, null=True, default=0.0)
	city = models.CharField(max_length=30, blank=True, null=True)
	date_of_birth = models.DateTimeField(blank=True, null=True)
	phone_number = models.CharField(max_length=10,blank=False, null=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = "Author"
		verbose_name_plural = "Authors"

class Review(models.Model):
	heading = models.CharField(max_length=50, blank=False, null=False)
	main_text = models.TextField(max_length=250, blank=False, null=False)
	stars = models.IntegerField(default=0, blank=False, null=False)

	def __unicode__(self):
		return self.heading + " " + self.stars

	class Meta:
		verbose_name = "Review"
		verbose_name_plural = "Reviews"
