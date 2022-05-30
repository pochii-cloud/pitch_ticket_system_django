from datetime import datetime, date

from django.db import models


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveBigIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Fields'


class Team(models.Model):
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Teams'


class Fixture(models.Model):
    TeamA = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='TeamA')
    TeamB = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='TeamB')
    Date = models.DateField(auto_now_add=False, null=True, help_text='dd//mm//yy')
    Time = models.TimeField(auto_now_add=False, null=True, help_text='Ex:02:00')
    Booked = models.BooleanField(default=False)
    Ground = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.TeamA) + ":" + str('Vs') + ":" + str(self.TeamB)

    def get_days_remaining_to_match(self, pk):
        # gets the days remaining for the match to start
        fixture = Fixture.objects.get(pk=pk)
        today = date.today()
        days = fixture.Date - today
        fixture.save()
        return days


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'
