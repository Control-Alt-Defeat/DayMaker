from django.forms import Form, ModelForm, TimeInput, ModelChoiceField, RadioSelect
from .models import Event, EventFinder

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
        widgets = {
            'start_time': TimeInput,
            'end_time': TimeInput,
        }

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


class EventFinderForm(ModelForm):
    class Meta:
        model = EventFinder
        fields = [
            'loc_type',
            'price',
            'min_rating',
            'start_time',
            'end_time',
            'result_count',
            'search_radius',
            'lat_coord',
            'long_coord',
            ]
        
    def __init__(self, *args, **kwargs):
        super(EventFinderForm, self).__init__(*args, **kwargs)
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control'})
        self.fields['min_rating'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['result_count'].widget.attrs.update({'class' : 'form-control'})
        self.fields['search_radius'].widget.attrs.update({'class' : 'form-control'})
        self.fields['lat_coord'].widget.attrs.update({'class' : 'hidden'})
        self.fields['long_coord'].widget.attrs.update({'class' : 'hidden'})
        self.fields['lat_coord'].label = ''
        self.fields['long_coord'].label = ''
