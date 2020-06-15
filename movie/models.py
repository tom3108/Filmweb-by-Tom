from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ExtraInfo (models.Model):
	KIND = {

		(0,'Other'),
		(1,'Horror'),
		(2,'Dama'),

	}

	length = models.PositiveSmallIntegerField(default=0)
	kind = models.PositiveSmallIntegerField(default=0, choices=KIND)

class Movie (models.Model):
	title = models.CharField(max_length=100)
	title_eng = models.CharField(max_length=100, default='default')
	content = models.TextField()
	director = models.CharField(max_length=100, default='default')
	date_premiere = models.DateField(null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	year = models.PositiveSmallIntegerField(default=2000)
	imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	poster = models.ImageField(upload_to="poster", null=True, blank=True)
	extra = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null=True, blank=True)


	def __str__(self):
		return self.title
		
	def title_with_year(self):
		return "{} ({})".format(self.title, self.year)

	def get_absolute_url(self):
		return reverse('movie-detail', kwargs={'pk': self.pk})

class Rate(models.Model):
	review = models.TextField(default="", blank=True)
	stars = models.PositiveSmallIntegerField(default=5)
	film = models.ForeignKey(Movie, on_delete=models.CASCADE)

