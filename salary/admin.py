from django.contrib import admin

from salary.models import Employee

admin.site.register(Employee)

from salary.models import Book

admin.site.register(Book)

# Register your models here.
