from django.forms import Form, ModelForm, TimeInput, ModelChoiceField, RadioSelect
from .models import Event, EventFinder


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
        widgets = {
            'start_time': TimeInput,
            'end_time': TimeInput,
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['loc_name'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['loc_type'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control form-control-lg'})
        self.fields['rating'].widget.attrs.update({'class' : 'form-control form-control-lg'})


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
