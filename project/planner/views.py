import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Event, EventFinder, Plan
from .forms import EventForm, EventFinderForm, PlanForm
from .DayMaker import natLangQuery, buildRule, andRule, groupRule



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
    Event.delete_hidden()
    event_list = list(Event.objects.filter(plan_id=plan_id, show=True).order_by('start_time'))
    event_list_json = [event.json() for event in event_list]
    template_name = 'planner/index.html'
    context = {
        'event_list': event_list,
        'event_list_json': json.dumps(event_list_json),
        'plan_id': plan_id
    }
    return render(request, template_name, context)

def add_event(request,plan_id):
    template_name = 'planner/add_event.html'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            event = form.save()
            event.plan = Plan.objects.get(id = plan_id)
            event.save()
            # redirect to a new URL:
            return redirect('planner:index', plan_id=plan_id)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()
        context = {
            'form': form,
            'plan_id':plan_id
        }

    return render(request, template_name, context)

def find_event(request,plan_id):
    template_name = 'eventFinderForm.html'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventFinderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
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
            return display_results(request, plan_id, results['results'], start_time, end_time)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventFinderForm()
        context = {
        'form': form,
        'plan_id': plan_id
        }

    return render(request, template_name, context)

def display_results(request,plan_id, search_results=None, start_time=None, end_time=None):
    template_name = 'planner/search_results.html'

    if request.method == 'POST':
        # get key of selected event from the request
        if 'choice' not in request.POST:
            return redirect('planner:plan')
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
            'search_results' : search_results_json,
            'plan_id': plan_id
        }
        return render(request, template_name, context)


class EventDelete(DeleteView):
    model = Event
    template_name = 'planner/confirm_delete.html'
    success_url = None

    def __init__(self):
        self.success_url = self.get_object().plan.id;

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
