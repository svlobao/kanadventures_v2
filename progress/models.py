import uuid

from django.db import models


class Progress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quizzes_answered = models.PositiveSmallIntegerField()
    quizzes_correct = models.PositiveSmallIntegerField()
    words_seen = models.PositiveIntegerField()
    phrase_seen = models.PositiveIntegerField()
    days_registered = models.PositiveIntegerField()
    days_consecutive = models.PositiveIntegerField()
    jlpt = models.CharField(max_length=2, default="")
