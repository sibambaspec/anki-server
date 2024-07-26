from django.db import models

# Create your models here.
from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
