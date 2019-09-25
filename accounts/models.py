from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# display balance of each user
class balance(models.Model):
    #    user = models.ForeignKey(User)
       balance = models.IntegerField(default = 0)