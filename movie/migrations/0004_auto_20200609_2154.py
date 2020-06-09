# Generated by Django 3.0.4 on 2020-06-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200608_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='poster',
        ),
        migrations.AddField(
            model_name='movie',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
