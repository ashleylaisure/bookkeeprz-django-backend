# Generated by Django 5.2.3 on 2025-07-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_journal_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
