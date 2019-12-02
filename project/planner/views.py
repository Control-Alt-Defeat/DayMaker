import json
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView, UpdateView
from decimal import Decimal

from .models import Event, EventFinder, Plan
from .forms import EventForm, EventFinderForm, PlanForm
from .DayMaker import natLangQuery, getTags
from .rules import build_query_filter
from .distance import distance


def load_categories(request):
    template_name = 'planner/category_dropdown_list_options.html'
    loc_type = request.GET.get('loc_type')
    categories = getTags(loc_type)
    return render(request, template_name, {'categories': categories})

# return true if NO overlap. return False if overlap.
def checkEventOverlap(start_time, end_time, plan_id):
    event_list = list(Event.objects.filter(plan_id = Plan.objects.get(id = plan_id), show=True).order_by('start_time'))

    times = [(event.start_time, event.end_time) for event in event_list]
    for timeSet in times:
        if timeSet[1] > start_time and timeSet[1] <= end_time:         # end time of existing event inside of time range
            return False
        if timeSet[1] > start_time and timeSet[1] > end_time and timeSet[0] <= start_time:  # time range inside of existing event
            return False
        if timeSet[0] > start_time and timeSet[0] < end_time:       # start time of existing event inside of time range
            return False
        if timeSet[0] >= start_time and timeSet[1] < end_time:      # existing event insde of time range 
            return False
    return True

def checkValidTimeRange(start_time, end_time):
    if start_time < end_time:
        return True
    else:
        return False

#
# View Methods
#

def add_plan(request):
    template_name = 'planner/add_plan.html'
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save()
            plan.user = request.user
            plan.save()
            return redirect("planner:plan_index")
    else:
        form = PlanForm()
        return render(request, template_name, {'form': form})

def plan_index(request):
    plan_list = list(Plan.objects.filter(user = request.user))
    template_name = 'planner/plan_index.html'
    context = {
        'plan_list': plan_list,
    }
    return render(request, template_name, context)

def home(request):
    return render(request,'home.html')

def index(request, plan_id):
    template_name = 'planner/event_index.html'

    Event.delete_hidden()
    EventFinder.delete_searches(request.user)

    event_list = list(Event.objects.filter(plan_id = Plan.objects.get(id = plan_id), show=True).order_by('start_time'))
    event_list_json = [event.json() for event in event_list]

    context = {
        'event_list': event_list,
        'event_list_json': json.dumps(event_list_json),
        'plan_id': plan_id
    }

    return render(request, template_name, context)

def add_event(request, plan_id):
    template_name = 'planner/add_event.html'
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            
            valid = True
            # check for valid time range
            if not checkValidTimeRange(start_time, end_time):
                valid = False
                context['timeError'] = 'Time Error!'
            # check for overlapping event
            if not checkEventOverlap(start_time, end_time, plan_id):
               valid = False
               context['eventOverlap'] = 'Event Overlap!'
            # if valid redirect to results
            if valid:
                event = form.save()
                event.plan = Plan.objects.get(id = plan_id)
                event.save()
                # redirect to a new URL:
                return redirect('planner:index', plan_id=plan_id)
            # if not valid, reload form through default render
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    context['form'] = form
    context['plan_id'] = plan_id

    return render(request, template_name, context)

def find_event(request, plan_id):
    template_name = 'planner/event_finder.html'
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventFinderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            loc_type = form.cleaned_data['loc_type']
            loc_category = form.cleaned_data['loc_category']
            price = form.cleaned_data['price']
            min_rating = form.cleaned_data['min_rating']
            num_results = form.cleaned_data['result_count']
            max_distance = form.cleaned_data['search_radius']
            lat_coord = form.cleaned_data['lat_coord']
            long_coord = form.cleaned_data['long_coord']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            search = form.save()
            search.user = request.user
            search.save()

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

            request.method = 'GET'

            valid = True
            # check for valid time range
            if not checkValidTimeRange(start_time, end_time):
                valid = False
                context['timeError'] = 'Time Error!'
            # check for overlapping event
            if not checkEventOverlap(start_time, end_time, plan_id):
               valid = False
               context['eventOverlap'] = 'Event Overlap!'
            # if valid redirect to results
            if valid:
                results = natLangQuery(
                    query_str = loc_category,
                    query_filter = query_filter,
                    num_results = num_results,
                    distance = max_distance,
                    aCoord = coords,
                    timeframe = timeframe,
                    query_tgt = loc_type
                )
                return display_results(request, plan_id, lat_coord, long_coord, results['results'], start_time, end_time)
            # if not valid, reload form with base render
            else:
                context['category'] = loc_category
    # if a GET (or any other method) we'll create a blank form
    else:
        prev_search = None
        query = EventFinder.objects.filter(user=request.user)
        if len(query) > 0:
            prev_search = query.latest('id')
            category = prev_search.loc_category
            if(category != ''):
                context['category'] = category

        form = EventFinderForm(instance=prev_search or None)

    context['form'] = form
    context['plan_id'] = plan_id
    return render(request, template_name, context)

def display_results(request, plan_id, user_lat_coord=None, user_long_coord=None, search_results=None, start_time=None, end_time=None):

    template_name = 'planner/search_results.html'

    if request.method == 'POST':
        # get key of selected event from the request
        if 'choice' not in request.POST:
            return redirect('planner:plan', plan_id=plan_id)
        search_key = int(request.POST['choice'])
        selected = Event.objects.get(pk=search_key)
        # set the selected event to show on the plan
        selected.show = True
        selected.plan = Plan.objects.get(id=plan_id)
        selected.save()
        # remove unnecesary hidden search results
        Event.delete_hidden()
        # redirect to the index url (home page)
        return redirect('planner:index', plan_id=plan_id)
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
                show = False
            )
            loc.save()
            location = loc.json()
            location['distance'] = distance(
                float(result['coordinates']['latitude']),
                float(result['coordinates']['longitude']),
                float(user_lat_coord),
                float(user_long_coord))
            search_results_json.append(location)
        search_results_json.sort(key = lambda x: x['distance'])
        context = {
            'search_results' : search_results_json,
            'plan_id': plan_id
        }
        
        return render(request, template_name, context)


class EventDelete(DeleteView):
    model = Event
    template_name = 'planner/confirm_delete.html'
    success_url = 'planner/index.html'

    def get_context_data(self, **kwargs):
        context = super(EventDelete, self).get_context_data(**kwargs)
        context['plan_id'] = self.kwargs.get("plan_id")
        return context

    def get_object(self):
        event_id = self.kwargs.get('event_id')

        return get_object_or_404(Event, id=event_id)

    def delete(self, request, *args, **kwargs):

        event = self.get_object()
        plan_id = event.plan.id
        event_id = event.id
        event = Event.objects.get(id = event_id)
        event.delete()

        return redirect('planner:index', plan_id=plan_id)


class EventUpdateView(UpdateView):
    template_name = 'planner/edit_event.html'
    form_class = EventForm

    def get_object(self):
        event_id = self.kwargs.get("event_id")
        return get_object_or_404(Event, id=event_id)

    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context['plan_id'] = self.kwargs.get("plan_id")
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
