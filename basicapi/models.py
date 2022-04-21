from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Note(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    attachments = ArrayField(
        ArrayField(models.CharField(max_length=255)),
        null=True,
        default=None
    )

    def __str__(self):
        return self.id
