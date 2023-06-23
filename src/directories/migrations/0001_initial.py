# Generated by Django 4.2.1 on 2023-06-23 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=50, verbose_name='Autor name')),
                ('autor_description', models.TextField(blank=True, null=True, verbose_name='Autor description')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50, verbose_name='Genre')),
                ('genre_description', models.TextField(blank=True, null=True, verbose_name='Genre description')),
            ],
        ),
        migrations.CreateModel(
            name='Publishing_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_house_name', models.CharField(max_length=50, verbose_name='Publishing house name')),
                ('publishing_house_description', models.TextField(blank=True, null=True, verbose_name='Publishing house description')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=100, verbose_name='Series')),
                ('series_description', models.TextField(blank=True, null=True, verbose_name="Count book's series")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, verbose_name='Book name')),
                ('book_image', models.ImageField(blank=True, default='/book/book-default.jpg', upload_to='book/%Y/%m/%d/')),
                ('book_price', models.DecimalField(decimal_places=2, default=0.01, max_digits=6)),
                ('year_publishing', models.DateField(max_length=50, verbose_name='Year publishing book')),
                ('page', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('binding', models.CharField(choices=[('Solid', 'solid'), ('Soft', 'soft'), ('Absent', 'absent')], max_length=6, verbose_name='Binding book')),
                ('format_book', models.CharField(choices=[('84x108/64', '84x108/64'), ('75x90/32', '75x90/32'), ('60x90/16', '60x90/16'), ('70x108/16', '70x108/16'), ('60x90/8', '60x90/8'), ('84x108/8', '84x108/8')], max_length=12, verbose_name='Book format')),
                ('ISBN', models.CharField(max_length=25, verbose_name='ISBN')),
                ('weight', models.DecimalField(decimal_places=1, default=0, max_digits=6, verbose_name='Book weight(gramme)')),
                ('age_restrictions', models.DecimalField(decimal_places=0, default=0, max_digits=3, verbose_name='Age restrictions')),
                ('counter_book', models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='Count of books available')),
                ('active', models.CharField(choices=[('Y', 'active'), ('N', 'inactive')], max_length=4, verbose_name='Book active')),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Rating')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.autor', verbose_name='autor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.genre', verbose_name='genre')),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directories.publishing_house', verbose_name='Publishing house')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directories.series', verbose_name='series')),
            ],
        ),
    ]
