from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Tables(models.Model):
    seats = models.IntegerField(
      default = 1,
      validators = [
         MaxValueValidator(13),
         MinValueValidator(1)
      ]
   )