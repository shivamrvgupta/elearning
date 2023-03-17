from django.db import models
from datetime import datetime

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    label = models.ImageField(upload_to='label/%Y/%m/%d/', blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Sub_Topic(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    label = models.ImageField(upload_to='sub-label/%Y/%m/%d/', blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name

class Video(models.Model):
    video = models.FileField(upload_to="videos/%Y/%m/%d/", max_length=100)
    topic = models.ForeignKey(Sub_Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descrption = models.TextField(blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name