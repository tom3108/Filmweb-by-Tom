# Generated by Django 3.0.4 on 2020-06-15 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20200615_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='kind',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (2, 'Dama'), (0, 'Other')], default=0),
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
    ]