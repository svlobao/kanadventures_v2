import uuid

from django.db import models
from vocabulary.models import Word


class Flashcard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.ChartField(max_length=200)
    back = models.ChartField(max_length=200)
