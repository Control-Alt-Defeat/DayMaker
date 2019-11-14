from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from .DayMaker import getTags

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
    loc_name = models.CharField('Name of Location', max_length=30)
    loc_type = models.CharField('Type of Location', max_length=30)
    address = models.CharField('Address of Location', max_length=30)
    lat_coord = models.DecimalField(max_digits=9, decimal_places=6, default=40.002287)
    long_coord = models.DecimalField(max_digits=9, decimal_places=6, default=-83.016017)
    phone_number = models.CharField('Business Phone Number', max_length=12, null=True)
    price = models.CharField(max_length=1, choices=PRICES, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField('start time of event')
    end_time = models.TimeField('end time of event')
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.loc_name
    
    def json(self):
        return {
            'id'           : self.id,
            'location'     : str(self.loc_name),
            'type'         : str(self.loc_type),
            'address'      : str(self.address),
            'phone_number' : str(self.phone_number),
            'price'        : self.get_price_display(),
            'rating'       : self.rating,
            'start'        : str(self.start_time),
            'end'          : str(self.end_time),
        }
    
    def delete_hidden():
        Event.objects.filter(show=False).delete()
    
    def get_absolute_url(self):
        return reverse('planner:index')

    def full_location(self):
        return {
            'latitude': self.lat_coord,
            'longitude': self.long_coord,
            'address': self.address,
        }


class EventFinder(models.Model):

    PRICES = (
        ('', 'Choose a price level'),
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$'),
    )
    TYPE = getTags()
    MIN_RATINGS = (
        ('', 'Choose a minimum rating'),
        ('1','★'),
        ('2','★★'),
        ('3','★★★'),
        ('4','★★★★'),
        ('5','★★★★★'),
    )
    TRANSPORTATION = (
        ('1','Walk'),
        ('2','Car'),
        ('3','Both'),
    )
    
    loc_type = models.CharField('Location Type', max_length=100, choices=TYPE, null=True, blank=True)   
    price = models.CharField(max_length=1, choices=PRICES, null=True, blank=True, default='')
    min_rating = models.CharField('Minimum Rating', max_length=1, choices=MIN_RATINGS, null=True, blank=True, default='')
    transportation = models.CharField('Mode of Transportation', max_length=1, choices=TRANSPORTATION, null=True, blank=True)
    result_count = models.PositiveIntegerField('Number of Search Results', default=3, validators=[MinValueValidator(1), MaxValueValidator(50)])
    start_time = models.TimeField('Start Time of Event', default='12:00', null=True, blank=True)
    end_time = models.TimeField('End Time of Event', default='12:30', null=True, blank=True)
    search_radius = models.FloatField('Search Radius(in miles)', default=5)
    lat_coord = models.DecimalField(max_digits=9, decimal_places=6, default=40.002287)
    long_coord = models.DecimalField(max_digits=9, decimal_places=6, default=-83.016017)

    def __str__(self):
        return f'Query {self.id}: {self.start_time} - {self.start_time}'
