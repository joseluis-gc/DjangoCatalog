from django.contrib import admin
from django.utils.html import format_html
from cars.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;">'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'car_title', 'model', 'year', 'color', 'body_style', 'fuel_type', 'city', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type',)
    list_filter = ('city', 'model',)


admin.site.register(Car, CarAdmin)
