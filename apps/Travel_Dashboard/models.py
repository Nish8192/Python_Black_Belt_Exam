from __future__ import unicode_literals
import re
from datetime import date, datetime
from django.db import models
from ..Login_Register.models import User

class TripManager(models.Manager):
    def validTravelDate(self, date):
        today = datetime.strptime(str(date.today())[:10], '%Y-%m-%d')
        difference = (date - today).days
        if difference <= 0:
            return False
        else:
            return True
    def validDates(self, depDate, arrDate):
        difference = (arrDate - depDate).days
        if difference <= 0:
            return False
        else:
            return True

class Trip(models.Model):
    destination = models.CharField(max_length = 100)
    startDate = models.DateField()
    endDate = models.DateField()
    plan = models.CharField(max_length = 1000)
    users = models.ForeignKey(User, related_name = 'users_on_trip')
    objects = TripManager()

class UserAndTrip(models.Model):
    users = models.ForeignKey(User, related_name = 'user_going')
    trips = models.ForeignKey(Trip, related_name = 'trip_going')
