
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event, EventForm, EventFinder, EventFinderForm
import json


def index(request):
    event_list = Event.objects.order_by('-start_time')
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

def add_eventfinder(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventFinderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            price = form.cleaned_data['price']
            type = form.cleaned_data['type']
            return HttpResponse('Type:' + type + "\Price: "+ price)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventFinderForm()

    return render(request, 'eventFinderForm.html', {'form': form})


# def add_event(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = EventForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             return HttpResponse('Success!')#DO SOMETHING HERE

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = EventForm()

#     return render(request, 'eventForm.html', {'form': form})
