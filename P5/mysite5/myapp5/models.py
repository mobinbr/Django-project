from django.db import models
from django.db.models.query_utils import select_related_descend

class Poem(models.Model):
    poem_name = models.CharField(max_length=128)
    poet_name = models.CharField(max_length=128)
    age = models.CharField(max_length=128)
    poem = models.TextField()

    def __str__(self) -> str:
        return self.poem_name

