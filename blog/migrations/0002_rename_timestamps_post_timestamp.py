# Generated by Django 3.2.4 on 2021-06-25 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timestamps',
            new_name='timestamp',
        ),
    ]
