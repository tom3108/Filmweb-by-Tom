from django.contrib import admin
from .models import Movie, ExtraInfo, Rate, Actor

admin.site.register(Movie)
# Register your models here.

admin.site.register(ExtraInfo)


admin.site.register(Rate)

admin.site.register(Actor)