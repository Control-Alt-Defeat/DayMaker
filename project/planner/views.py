import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from decimal import Decimal

from .models import Event, EventFinder
from .forms import EventForm, EventFinderForm
from .DayMaker import natLangQuery
from .rules import build_query_filter
from .distance import distance




def index(request):
    Event.delete_hidden()
    event_list = Event.objects.filter(show=True).order_by('start_time')
    event_list_json = [event.json() for event in event_list]
    template_name = 'planner/index.html'
    context = {
        'event_list': event_list,
        'event_list_json': json.dumps(event_list_json)
    }
    return render(request, template_name, context)

def add_event(request):
    template_name = 'planner/add_event.html'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('planner:index')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    return render(request, template_name, {'form': form})

def find_event(request):
    template_name = 'planner/eventFinderForm.html'
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventFinderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            loc_type = form.cleaned_data['loc_type']
            price = form.cleaned_data['price']
            min_rating = form.cleaned_data['min_rating']
            num_results = form.cleaned_data['result_count']
            max_distance = form.cleaned_data['search_radius']
            lat_coord = form.cleaned_data['lat_coord']
            long_coord = form.cleaned_data['long_coord']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            query_filter = build_query_filter(price, min_rating)
            coords = {
                'latitude': lat_coord,
                'longitude': long_coord,
            }
            timeframe = {
                'start_time': start_time,
                'end_time': end_time,
                'date': '11-13-2019',
            }

            #import pdb; pdb.set_trace()
            results = natLangQuery(
                loc_type,
                query_filter,
                num_results,
                max_distance,
                coords,
                timeframe
            )

            request.method = 'GET'
            return display_results(request,lat_coord,long_coord,results['results'], start_time, end_time)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventFinderForm()
    
    context['form'] = form
    return render(request, template_name, context)

def display_results(request,user_lat_coord=None,user_long_coord=None, search_results=None, start_time=None, end_time=None,):
    template_name = 'planner/search_results.html'
    
    
    if request.method == 'POST':
        # get key of selected event from the request
        if 'choice' not in request.POST:
            return redirect('planner:plan')
        search_key = int(request.POST['choice'])
        selected = Event.objects.get(pk=search_key)
        # set the selected event to show on the plan
        selected.show = True
        selected.save()
        # remove unnecesary hidden search results
        Event.delete_hidden()
        # redirect to the index url (home page)
        return redirect('planner:index')
    else:
        search_results_json = []
        for result in search_results:
            loc = Event(
                loc_name = result['name'],
                loc_type = result['categories'][0]['title'],
                address = result['location']['address1'],
                lat_coord = result['coordinates']['latitude'],
                long_coord = result['coordinates']['longitude'],
                phone_number = result['phone'],
                price = result['price'] if 'price' in result else None,
                rating = result['rating'],
                start_time = start_time,
                end_time = end_time,
                show=False
                
            )
            loc.save()
            location = loc.json()
            location['distance'] = distance(float(result['coordinates']['latitude']),float(result['coordinates']['longitude']),float(user_lat_coord),float(user_long_coord))
            search_results_json.append(location)
        search_results_json.sort(key = lambda x: x['distance'])
        context = {
            'search_results' : search_results_json
        }
        
        return render(request, template_name, context)

def get_date_of_plan(request):
 	response = {'dateOfPlan': None}
 	response['dateOfPlan'] = datetime.datetime.now().strftime("%B %d, %Y")
 	return HttpResponse(json.dumps(response), content_type="application/json")

class EventDelete(DeleteView):
    model = Event
    template_name = 'planner/confirm_delete.html'
    success_url = reverse_lazy('planner:index')

    def get_object(self):
        event_id = self.kwargs.get('event_id')
        return get_object_or_404(Event, id=event_id)


class EventUpdateView(UpdateView):
    template_name = 'planner/add_event.html'
    form_class = EventForm

    def get_object(self):
        event_id = self.kwargs.get("event_id")
        return get_object_or_404(Event, id=event_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
