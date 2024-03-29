from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
import json
import datetime


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


def home(request, template_name="home.html"):
	context = {'title': 'DayMaker - Home'}
	return render_to_response(template_name, context)

def chat(request, template_name="chat.html"):
	context = {'title': 'DayMaker Chat Version 1.0'}
	return render_to_response(template_name, context)

def get_date_of_plan(request):
	response = {'dateOfPlan': None}
	response['dateOfPlan'] = datetime.datetime.now().strftime("%B %d, %Y")
	return HttpResponse(json.dumps(response), content_type="application/json")