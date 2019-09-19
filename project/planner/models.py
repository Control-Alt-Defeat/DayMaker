from django.db import models

# Create your models here.

class Plan(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateTimeField('date planned')

class Event(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    loc_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    loc_type = models.CharField(max_length=30)
    start_time = models.DateTimeField('start time of event')
    end_time = models.DateTimeField('end time of event')
    cost = models.IntegerField()
    rating = models.IntegerField()

    def __init__(self, name, id):
        self.title = name
        self.id = id

    def addAddress(self, address):
        self.location = address


