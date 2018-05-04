# apps/books/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Course(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "Curso"

    def __str__(self):
        return self.name


class Editorial(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.name


class Kind(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "Tipo"

    def __str__(self):
        return self.name


class Pdf(TimeStampedModel):
    available = models.BooleanField(default=True, verbose_name="disponible")
    course = models.ForeignKey("Course", verbose_name="curso")
    kind = models.ForeignKey("Kind", verbose_name="tipo")
    name = models.CharField(max_length=50, verbose_name="nombre")
    topic = models.ManyToManyField("Topic", verbose_name="tema")
    url = models.URLField(verbose_name="link")

    def __str__(self):
        return self.name


class Topic(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name="nombre")

    def __str__(self):
        return self.name
