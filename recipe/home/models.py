from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    recipe_count = models.IntegerField(default=50)

    def __str__(self):
        return self.recipe_name

import random

# for recipe in recipes:
#     recipe.recipe_count = random.randint(10, 100)
#     recipe.save()
