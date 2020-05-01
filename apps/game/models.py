from django.db import models
from apps.category.models import Category


class Game(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30)
    image = models.FileField(null=False, blank=False, upload_to='gameImage')
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
