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

class Photograph(ArchiveDocument):
    creator = models.TextField(max_length = 50, blank=True, null= False, default = 'Lois, Lauren, and Julia')
    record_type = models.TextField(blank = True, null = False, max_length=200)
    color = models.TextField(blank = True, null = False, max_length=100)
    medium = models.TextField(blank = True, null = False, max_length=100)
    image_content = models.TextField(blank = True, null = False, max_length=300)
    language = models.TextField(blank = True, null = False, max_length=200)

class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    transcription = models.TextField(blank=True, null=False)
