from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    description = models.CharField(max_length=1000, blank=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description