from django.shortcuts import render
from .models import Event, EventForm, EventFinder, EventFinderForm
from django.http import HttpResponseRedirect, HttpResponse




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

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


def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponse('Success!')#DO SOMETHING HERE

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    return render(request, 'eventForm.html', {'form': form})
