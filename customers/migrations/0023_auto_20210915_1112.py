# Generated by Django 3.2.7 on 2021-09-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0022_alter_image_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
