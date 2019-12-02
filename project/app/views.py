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
	data = {
		'lat': location.latitude if location else None,
		'long': location.longitude if location else None,
		'msg': f'Valid Location! Latitude: {location.latitude}°, Longitude: {location.longitude}°' if location else 'Invalid Location, please try a different address'
	}

	return JsonResponse(data)

@csrf_exempt
def get_date_of_plan(request):
	response = {'dateOfPlan': datetime.datetime.now().strftime("%B %d, %Y")}
	return JsonResponse(response)

@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body)
		message = data['message']

		# chat_response = chatbot.get_response(message).text
		chat_response = "Chatbot not home, you said: " + message
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)

class NewPlanFormView(CreateView):
	model = Plan
	form_class = PlanForm
	template_name = 'planner/add_plan.html'

	def post(self, request):
		form = PlanForm(request.POST)
		if form.is_valid():
			plan = form.save()
			plan.user = request.user
			plan.save()
			return redirect("planner:plan_index")
		else:
			context = { 'form': form }
			return render(request, 'newPlanForm.html', context=context)

