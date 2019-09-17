from django.db import models

# Create your models here.

class Event(models.Model):
    location = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __init__(self, name, id):
        self.title = name
        self.id = id


    def addAddress(self, address):
        self.location = address