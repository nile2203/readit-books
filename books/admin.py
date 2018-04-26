# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
	list_display=('title','author')

admin.site.register(Books, BooksAdmin)
