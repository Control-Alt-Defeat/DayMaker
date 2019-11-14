import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Event, EventFinder
from .forms import EventForm, EventFinderForm
from .DayMaker import natLangQuery, buildRule, andRule, groupRule


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
    template_name = 'eventFinderForm.html'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventFinderForm(request.POST)
        # check whether it's valid:
        if True:
            loc_type = form.cleaned_data['loc_type']
            price = form.cleaned_data['price']

            if (price == '1'):
                price = '$'
            elif (price == '2'):
                price = '$$'
            elif (price == '3'):
                price = '$$$' 

            min_rating = form.cleaned_data['min_rating']
            num_results = form.cleaned_data['result_count']
            
            price_rule, rate_rule, query_filter = None, None, None

            if price:
                price_rule = groupRule(buildRule('price', price, '::'))
            if min_rating:
                rate_rule = groupRule(buildRule('rating', int(min_rating), '>='))
            if price_rule and rate_rule:
                query_filter = andRule(price_rule, rate_rule)
            elif price_rule or rate_rule:
                query_filter = price_rule if price_rule else rate_rule
            else:
                query_filter = ""

            results = natLangQuery(loc_type, query_filter, num_results)

            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            request.method = 'GET'
            return display_results(request, results['results'], start_time, end_time)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventFinderForm()

    return render(request, template_name, {'form': form})

def display_results(request, search_results=None, start_time=None, end_time=None):
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
                phone_number = result['phone'],
                price = result['price'] if 'price' in result else None,
                rating = result['rating'],
                start_time = start_time,
                end_time = end_time,
                show=False
            )
            loc.save()
            search_results_json.append(loc.json())
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