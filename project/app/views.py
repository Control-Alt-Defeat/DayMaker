from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
import json
import datetime
from django.views.generic import TemplateView, CreateView, DetailView, FormView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from planner.forms import PlanForm 
from planner.models import Plan


@csrf_exempt
def check_address(request):
    address = request.GET.get('address', None)
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)
    if location:
        lat_display = '%.4f'%(location.latitude)
        long_display = '%.4f'%(location.longitude)
    data = {
        'lat': location.latitude if location else None,
        'long': location.longitude if location else None,
        'msg': f'Valid Location! Latitude: {lat_display}°, Longitude: {long_display}°' if location else 'Invalid Location, please try a different address'
    }

    return JsonResponse(data)

@csrf_exempt
def get_date_of_plan(request):
    response = {'dateOfPlan': datetime.datetime.now().strftime("%B %d, %Y")}
    return JsonResponse(response)
