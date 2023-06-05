# Generated by Django 4.2.1 on 2023-06-05 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.autor', verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.genre', verbose_name='genre'),
        ),
    ]