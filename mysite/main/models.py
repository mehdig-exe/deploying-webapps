from django.db import models
from datetime import datetime
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = HTMLField()
    tutorial_published = models.DateTimeField("date published", default= timezone.now())

    def __str__(self):
        return self.tutorial_title