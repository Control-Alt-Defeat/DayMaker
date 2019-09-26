from django.db import models
from django.forms import ModelForm

# Create your models here.

class EventFinder(models.Model):
    PRICES = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$')
    )
    TYPE = (
        ('1','Food'),('2','Bar'),('3','Movie'))
    SIZE = (
        ('1','1'),('2','2-3'),('3','4+'))
    TRANSPORTATION = (('1','Walk'),('2','Car'),('3','Both'))
    
    type = models.CharField(max_length=1, choices=TYPE)   
    price = models.CharField(max_length=1, choices=PRICES)
    size = models.CharField(max_length=1, choices=SIZE)
    transportation = models.CharField(max_length=1, choices =TRANSPORTATION)
    
    

class EventFinderForm(ModelForm):
    class Meta:
        model = EventFinder
        fields = ['type','price','size','transportation']
        
    def __init__(self, *args, **kwargs):
        super(EventFinderForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['type'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['size'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['transportation'].widget.attrs.update({'class' : 'form-control form-control-lg'})

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

    def addAddress(self, address):
        self.location = address
        
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'loc_name', 
            'loc_type', 
            'address',  
            'start_time',
            'end_time',
            'cost',
            'rating'
            ]
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['loc_name'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['cost'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['rating'].widget.attrs.update({'class' : 'form-control form-control-lg'})
       
    




