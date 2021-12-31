from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):
    state_choice = (
        ('CA', 'California'),
        ('AZ', 'Arizona'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    features_choices = (
        ('Apple Android Play', 'Apple Android Play'),
        ('Camera', 'Camera'),
        ('A/C', 'A/C'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=255)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    miles = models.CharField(max_length=255)
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=255)
    millage = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    no_of_owners = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title

