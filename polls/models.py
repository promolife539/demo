from django.db import models
from django.contrib.auth import get_user_model
from django import forms
import datetime
from django.utils import timezone

class Citizen(models.Model):
    citizen_id = models.PositiveIntegerField()
    town = models.CharField(max_length = 200)
    # street = models.CharField(max_length = 200)
    # building = models.CharField(max_length = 200)
    # apartment = models.PositiveIntegerField()
    # name = models.CharField(max_length = 200)
    # birth_date = models.CharField(max_length = 200)
    # GENDER = (
    # 	(1 , 'male'),
    # 	(2 , 'female'),
    # 	)
    # gender = models.PositiveSmallIntegerField(choices = GENDER)
    # relatives = models.

# Create your models here.

