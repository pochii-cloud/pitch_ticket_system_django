import random

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from core.models import Fixture


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=100)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    ticket_no = models.PositiveIntegerField(default=0)
    persons = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Reservations'
