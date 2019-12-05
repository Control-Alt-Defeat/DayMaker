import datetime
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from .DayMaker import getTags

# Create your models here.


class Plan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('date planned', default=datetime.date.today)
    name = models.CharField('name', max_length=30, default='My Plan', blank=True)
    
    def get_absolute_url(self):
        return reverse('planner:plan_index')

class Event(models.Model):
    PRICES = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$')
    )
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default = 1)
    loc_name = models.CharField('Name of Location', max_length=50)
    loc_type = models.CharField('Type of Location', max_length=50)
    address = models.CharField('Address of Location', max_length=80)
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
            'id'                : self.id,
            'plan_id'           : self.plan.id,
            'location'          : str(self.loc_name),
            'type'              : str(self.loc_type),
            'address'           : str(self.address),
            'phone_number'      : str(self.phone_number),
            'price'             : self.get_price_display(),
            'rating'            : self.rating,
            'start'             : str(self.start_time),
            'end'               : str(self.end_time),
            'start_formatted'   : str(self.convertTime(self.start_time)),
            'end_formatted'     : str(self.convertTime(self.end_time)),
        }

    def delete_hidden():
        Event.objects.filter(show=False).delete()

    def get_absolute_url(self):
        return reverse('planner:index', kwargs={'plan_id':self.plan.id})

    def full_location(self):
        return {
            'latitude': self.lat_coord,
            'longitude': self.long_coord,
            'address': self.address,
        }

    def convertTime(self, time):
        hour = time.strftime("%I")
        time = time.strftime("%I:%M %p") 
        if int(hour) < 10: 
            time = time[1:]
        return time


class EventFinder(models.Model):

    TYPES = (
        ('restaurants', 'Restaurants'),
        ('bars', 'Bars'),
        ('arts & entertainment', 'Arts & Entertainment')
    )
    PRICES = (
        ('', 'Choose a price level'),
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$'),
    )
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

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField('Where would you like to search?', max_length=100)
    loc_type = models.CharField('Location Type', max_length=100, choices=TYPES)
    loc_category = models.CharField('Location Category', max_length=100, null=True, blank=True)
    price = models.CharField(max_length=1, choices=PRICES, blank=True, default='')
    min_rating = models.CharField('Minimum Rating', max_length=1, choices=MIN_RATINGS, null=True, blank=True)
    transportation = models.CharField('Mode of Transportation', max_length=1, choices=TRANSPORTATION, null=True, blank=True)
    result_count = models.PositiveIntegerField('Number of Search Results', default=3, validators=[MinValueValidator(1), MaxValueValidator(50)])
    start_time = models.TimeField('Start Time of Event')
    end_time = models.TimeField('End Time of Event')
    search_radius = models.FloatField('Max Distance Away (in miles)', default=10, null=True, blank=True)
    lat_coord = models.DecimalField(max_digits=9, decimal_places=6, default=40.002287)
    long_coord = models.DecimalField(max_digits=9, decimal_places=6, default=-83.016017)

    def __str__(self):
        return f'Query {self.id}: {self.start_time} - {self.start_time}'

    def delete_searches(user_id):
        EventFinder.objects.filter(user=user_id).delete()
