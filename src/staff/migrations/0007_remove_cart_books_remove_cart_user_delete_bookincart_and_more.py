# Generated by Django 4.2.1 on 2023-06-16 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_cart_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='books',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='BookInCart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]