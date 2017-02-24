from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30, default="Bane")
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    img = models.CharField(max_length=1000, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
