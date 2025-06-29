import uuid

from django.db import models


class Phrase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phrase = models.CharField(max_length=300, unique=True)
    phrase_kana = models.CharField(max_length=300, default="")
    english_translation = models.CharField(max_length=300, default="")
