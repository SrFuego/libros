# apps/books/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Collection(TimeStampedModel):
    editorial = models.ForeignKey("Editorial")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Editorial(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Kind(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pdf(TimeStampedModel):
    available = models.BooleanField(default=True)
    collection = models.ForeignKey("Collection")
    course = models.ForeignKey("Course")
    kind = models.ForeignKey("Kind")
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name
