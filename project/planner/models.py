from django.db import models
from django.forms import ModelForm

# Create your models here.

class Plan(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateTimeField('date planned')

class Event(models.Model):
    PRICES = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$')
    )
    #plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    loc_name = models.CharField('name of location', max_length=30)
    loc_type = models.CharField('type of location', max_length=30)
    address = models.CharField('address of location', max_length=30)
    phone_number = models.CharField('callable phone number', max_length=12)
    price = models.CharField(max_length=1, choices=PRICES)
    rating = models.IntegerField()
    start_time = models.DateTimeField('start time of event')
    end_time = models.DateTimeField('end time of event')

    def __str__(self):
        return self.loc_name


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'loc_name', 
            'loc_type', 
            'address', 
            'phone_number', 
            'start_time',
            'end_time',
            ]


