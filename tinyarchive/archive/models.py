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
    description = models.TextField(blank=True, null=False, max_length=500)
    creator = models.CharField(max_length = 50, blank=True, null= False)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=True,
        blank = True,
    )

class Photograph(ArchiveDocument):
    record_type = models.CharField(blank = True, null = False, max_length=200)
    color = models.CharField(blank = True, null = False, max_length=100)
    medium = models.CharField(blank = True, null = False, max_length=100)
    image_content = models.CharField(blank = True, null = False, max_length=300)
    language = models.CharField(blank = True, null = False, max_length=200)
    threed = models.URLField(max_length=500, blank="True")
    photo_type = models.CharField(
        max_length=20,
        choices=list(
            Choices.PHOTO_TYPE_CHOICES.items()
        ),  # defining the constant as a dictionary for easy lookup in views.
    )

class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    transcription = models.TextField(blank=True, null=False)
