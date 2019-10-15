from django.db import models

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

    def __str__(self):
        return self.loc_name
    
    def json(self):
        return {
            'location'     : str(self.loc_name),
            'type'         : str(self.loc_type),
            'address'      : str(self.address),
            'phone_number' : str(self.phone_number),
            'price'        : self.get_price_display(),
            'rating'       : self.rating,
            'start'        : str(self.start_time),
            'end'          : str(self.end_time),
        }


class EventFinder(models.Model):

    PRICES = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$')
    )
    TYPE = (
        #('1','Food'),('2','Bar'),('3','Movie'))
        ('1','Mexican Food'), ('2','Ice Cream'), ('3','Coffee Shop'), ('4','Seafood'), ('5','Other Restaurants')
    )
    SIZE = (
        ('1','1'),('2','2-3'),('3','4+')
    )
    TRANSPORTATION = (
        ('1','Walk'), ('2','Car'), ('3','Both')
    )
    
    loc_type = models.CharField('Location Type', max_length=1, choices=TYPE)   
    price = models.CharField(max_length=1, choices=PRICES)
    size = models.CharField('Group Size', max_length=1, choices=SIZE)
    transportation = models.CharField('Mode of Transportation', max_length=1, choices =TRANSPORTATION)


# class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = [
#             'loc_name', 
#             'loc_type', 
#             'address', 
#             'phone_number', 
#             'start_time',
#             'end_time',
#             ]
#         widgets = {
#             'start_time': TimeInput,
#             'end_time': TimeInput,
#         }
