import uuid

from django.db import models


class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=50)
    kun = models.CharField(max_length=50, default="")
    on = models.CharField(max_length=50, default="")
    jlpt = models.CharField(max_length=2, default="")
    hinshi = models.CharField(max_length=20, default="")
    english_translation = models.CharField(max_length=100, default="")
