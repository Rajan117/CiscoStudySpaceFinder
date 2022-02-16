from django.db import models
import uuid
from django.template.defaultfilters import slugify



# Create your models here.

class StudySpace(models.Model):

    name = models.CharField(max_length=128, unique=True)
    avg_noise_level = models.FloatField(default=0)
    avg_light_level = models.FloatField(default=0)
    people = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'StudySpaces'

    def __str__(self):
        return self.name

class Device(models.Model):

    name = models.CharField(max_length=128, default='')
    location_tag = models.CharField(max_length=128, default='')
    device_type = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    serial = models.CharField(max_length=128, unique=True)
    net_ID = models.CharField(max_length=128)
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.serial)
        super(Device, self).save(*args, **kwargs)


class Search(models.Model):

    search_ID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=128)
    max_noise = models.IntegerField(default=0)
    min_noise = models.IntegerField(default=0)
    max_light = models.IntegerField(default=0)
    min_light = models.IntegerField(default=0)
    max_people = models.IntegerField(default=0)
    min_people = models.IntegerField(default=0)
    time = models.TimeField()
    date = models.DateField()

