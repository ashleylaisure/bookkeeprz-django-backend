# Generated by Django 5.2.3 on 2025-07-08 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_rename_date_added_book_created_book_modified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookshelf',
        ),
        migrations.DeleteModel(
            name='Bookshelf',
        ),
    ]
