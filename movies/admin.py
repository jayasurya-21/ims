from django.contrib import admin

# Register your models here.
from . models import MovieInfo,Director

admin.site.register(MovieInfo)
admin.site.register(Director)