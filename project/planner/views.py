import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event, EventFinder
from .forms import EventForm, EventFinderForm
from .DayMaker import natLangQuery


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
    template_name = 'add_event.html'
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

def edit_event(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def find_event(request):
    template_name = 'eventFinderForm.html'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventFinderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            price = form.cleaned_data['price']
            loc_type = form.cleaned_data['loc_type']
            num_results = form.cleaned_data['result_count']
            results = natLangQuery(loc_type, num_results)
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
