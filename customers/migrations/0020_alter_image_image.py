# Generated by Django 3.2.7 on 2021-09-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0019_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]