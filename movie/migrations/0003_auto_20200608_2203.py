# Generated by Django 3.0.4 on 2020-06-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200607_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='movie',
            name='date_premiere',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='poster'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
    ]
