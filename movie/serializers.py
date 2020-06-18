from django.contrib.auth.models import User
from rest_framework import serializers
from. models import Movie

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','email']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movie
		fields = ['title','content','year','imdb_rating']
