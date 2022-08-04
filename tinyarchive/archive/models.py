from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField
from stdimage import StdImageField
from archive.consts import *


class ArchiveDocument(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects=InheritanceManager()
    name = models.CharField(max_length=200)
    record_type = models.TextField(blank=True, null=False, max_length=100)
    color = models.TextField(blank=True, null=False, max_length=100)
    medium = models.TextField(blank=True, null=False, max_length=100)
    image_content = models.TextField(blank=True, null=False, max_length=100)
    description = models.TextField(blank=True, null=False, max_length=100)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
    )


class Photograph(ArchiveDocument):
    photo_type = models.CharField(
        max_length=20,
        choices=list(
            Choices.PHOTO_TYPE_CHOICES.items()
        ),  # defining the constant as a dictionary for easy lookup in views.
    )
