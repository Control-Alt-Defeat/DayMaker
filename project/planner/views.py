from django.shortcuts import render
#from django.http import HttpResponse
from .models import Event, EventForm


def index(request):
    event_list = Event.objects.order_by('-start_time')
    #template = loader.get_template('planner/index.html')
    context = {
        'event_list': event_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'planner/index.html', context)

def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/planner/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})

def edit_event(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
#
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)