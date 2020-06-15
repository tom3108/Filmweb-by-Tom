from django.contrib import admin
from .models import Movie, ExtraInfo

admin.site.register(Movie)
# Register your models here.

admin.site.register(ExtraInfo)
