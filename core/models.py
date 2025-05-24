from django.db import models
from django.utils.timezone import now


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    # 👈 ADD THIS

    def __str__(self):
        return self.name
