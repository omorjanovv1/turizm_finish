# Generated by Django 3.2.7 on 2021-09-11 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tours',
            new_name='Tour',
        ),
    ]