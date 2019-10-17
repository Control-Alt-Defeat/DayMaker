from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

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


class EventFinder(models.Model):

    PRICES = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$'),
    )
    TYPE = (
        ('1','Mexican'),
        ('2','Ice Cream'),
        ('3','Coffee Shop'),
        ('4','Seafood'),
        ('5','Other Restaurants'),
    )
    MIN_RATINGS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    TRANSPORTATION = (
        ('1','Walk'),
        ('2','Car'),
        ('3','Both'),
    )
    
    loc_type = models.CharField('Location Type', max_length=1, choices=TYPE, null=True, blank=True)   
    price = models.CharField(max_length=1, choices=PRICES, null=True, blank=True)
    min_rating = models.CharField('Group Size', max_length=1, choices=MIN_RATINGS, null=True, blank=True)
    transportation = models.CharField('Mode of Transportation', max_length=1, choices=TRANSPORTATION, null=True, blank=True)
    result_count = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(50)])
    start_time = models.TimeField('start time of event', default='12:00', null=True, blank=True)
    end_time = models.TimeField('end time of event', default='12:30', null=True, blank=True)

    def __str__(self):
        return f'Query {self.id}: {self.start_time} - {self.start_time}'