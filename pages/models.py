from django.db import models


# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') #pip install pillow
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    google_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' -Designation: ' + self.designation

