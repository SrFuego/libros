# apps/books/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Book(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
