# Generated by Django 4.0 on 2021-12-31 00:34

import ckeditor.fields
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_doors_alter_car_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Apple Android Play', 'Apple Android Play'), ('Camera', 'Camera'), ('A/C', 'A/C')], max_length=255),
        ),
    ]
