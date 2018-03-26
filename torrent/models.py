from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Tors(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    link = models.CharField(max_length=1000, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.author
