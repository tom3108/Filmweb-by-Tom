# Generated by Django 3.0.4 on 2020-06-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200612_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title_eng',
            field=models.CharField(default='default', max_length=100),
        ),
    ]