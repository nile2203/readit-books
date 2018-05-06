#- *- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
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
		(GENRE_SELF_HELP, 'self_help'),
		(GENRE_THRILLER, 'thriller'))

	STATUS_WANT_TO_READ = 'WANT_TO_READ'
	STATUS_CURRENTLY_READING = 'CURRENTLY_READING'
	STATUS_READ = 'READ'

	status_choices = (
		(STATUS_READ,'read'),
		(STATUS_WANT_TO_READ,'want_to_read'),
		(STATUS_CURRENTLY_READING,'currently_reading'),
	)

	title = models.CharField(max_length=150, blank=False)
	genre = models.CharField(max_length=30, blank=False, default=GENRE_FICTION, choices=genre_choices)
	date_reviewed = models.DateTimeField(default=None, blank=True, null=True)
	is_favourite = models.BooleanField(default=False, verbose_name="Favourite")
	authors = models.ManyToManyField("Author")
	review = models.ForeignKey("Review", null=True)
	status = models.CharField(max_length=20, blank=False, null=False, choices=status_choices, default=STATUS_WANT_TO_READ)

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

class BookShelf(models.Model):

	SHELF_TYPE_WANT_TO_READ = 'WANT_TO_READ'
	SHELF_TYPE_READ = 'READ'
	SHELF_TYPE_READING = 'READING'

	shelf_type_choices = (
		(SHELF_TYPE_READ, 'read'),
		(SHELF_TYPE_WANT_TO_READ, 'want_to_read'),
		(SHELF_TYPE_READING, 'reading'),
	)

	added_date = models.DateTimeField(blank=False, null=False, default=timezone.now())
	shelf_type = models.CharField(max_length=20, blank=False, null=False, default=SHELF_TYPE_WANT_TO_READ, choices=shelf_type_choices)

	def __unicode__(self):
		return self.shelf_type + " " + self.added_date

	class Meta:
		verbose_name = "Book Shelf"
		verbose_name_plural = "Book Shelves"

class Favourite(models.Model):

	added_date = models.DateTimeField(blank=False, null=False, default=timezone.now())
	book = models.ForeignKey('Books')

	def __unicode__(self):
		return self.book.title + " " + self.added_date

	class Meta:
		verbose_name = "Favourite"
		verbose_name_plural = "Favourites"
