import uuid

from django.db import models


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
