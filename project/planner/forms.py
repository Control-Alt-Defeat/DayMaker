import datetime
from django.forms import Form, ModelForm, TimeInput, ModelChoiceField, RadioSelect, TimeField
from .models import Event, EventFinder
from .widgets import SelectTimeWidget


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'loc_name', 
            'loc_type', 
            'address',  
            'start_time',
            'end_time',
            'price',
            'rating'
        ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['loc_name'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['rating'].widget.attrs.update({'class' : 'form-control form-control-lg'})

    start_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'Start Time')
    end_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'End Time')

class EventFinderForm(ModelForm):
    class Meta:
        model = EventFinder
        fields = [
            'loc_type',
            'price',
            'min_rating',
            'transportation',
            'start_time',
            'end_time',
            'result_count'
            ]
        
    def __init__(self, *args, **kwargs):
        super(EventFinderForm, self).__init__(*args, **kwargs)
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['min_rating'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['transportation'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['result_count'].widget.attrs.update({'class' : 'form-control form-control-lg'})
    
    start_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'Start Time')
    end_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'End Time')
    
    def is_valid(self, start_time, end_time):
        start = start_time.strmptime("%I:%M %p")
        end = end_time.strmptime("%I:%M %p")
        startHour = start.strftime("%I")
        endHour = end.strftime("%I")
        startMin = start.strftime("%M")
        endMin = end.strftime("%M")
        startM = start.strftime("%p")
        endM = end.strftime("%p")
        if startM == endM:
            if startHour > endHour:
                return False
            if startHour == endHour:
                if endMin - startM < 30:
                    return False
        elif startM == "AM":
            return False
        else:
            return False
        return True
