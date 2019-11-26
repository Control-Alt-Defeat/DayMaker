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
            'start_time',
            'end_time',
            'address',
            'lat_coord',
            'long_coord',
        ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['loc_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['lat_coord'].widget.attrs.update({'class' : 'hidden'})
        self.fields['long_coord'].widget.attrs.update({'class' : 'hidden'})
        self.fields['long_coord'].label = ''
        self.fields['lat_coord'].label = ''

    start_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'Start Time')
    end_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'End Time')
    
    
class EventFinderForm(ModelForm):
    class Meta:
        model = EventFinder
        fields = [
            'loc_type',
            'loc_category',
            'price',
            'min_rating',
            'start_time',
            'end_time',
            'result_count',
            'search_radius',
            'address',
            'lat_coord',
            'long_coord',
            ]
        
    def __init__(self, *args, **kwargs):
        super(EventFinderForm, self).__init__(*args, **kwargs)
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control'})
        self.fields['loc_category'].widget.attrs.update({'class' : 'form-control'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control'})
        self.fields['min_rating'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['result_count'].widget.attrs.update({'class' : 'form-control'})
        self.fields['search_radius'].widget.attrs.update({'class' : 'form-control'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control'})
        self.fields['lat_coord'].widget.attrs.update({'class' : 'hidden'})
        self.fields['long_coord'].widget.attrs.update({'class' : 'hidden'})
        self.fields['loc_category'].disabled = True
        self.fields['lat_coord'].label = ''
        self.fields['long_coord'].label = ''
    
    start_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'Start Time')
    end_time = TimeField(widget=SelectTimeWidget(twelve_hr=True, minute_step=15, use_seconds=False, required=False), required=False, label=u'End Time')
