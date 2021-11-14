from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class CustomUser(models.Model):

  def validate_not_empty(value):
         print("i'm in clean")
         if value == '' :
              raise ValidationError('Empty code not allowed')
  name = models.CharField(max_length=150)
  number = models.CharField(
    max_length=4,
unique=True
  )
   
  is_admin = models.BooleanField('admin status')
  password = models.CharField(max_length=100 , validators=[validate_not_empty])
  
  def __str__(self):
    return self.number
    