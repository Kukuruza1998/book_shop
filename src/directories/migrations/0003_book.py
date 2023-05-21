# Generated by Django 4.2.1 on 2023-05-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0002_autor_genre_publishing_house_series_delete_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, verbose_name='Book name')),
                ('book_image', models.ImageField(blank=True, upload_to='book')),
                ('book_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('year_publishing', models.DateField(max_length=50, verbose_name='Year publishing book')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directories.autor', verbose_name='autor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directories.genre', verbose_name='genre')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directories.series', verbose_name='series')),
            ],
        ),
    ]
