from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils.weather import get_weather
import json
from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from utils.wx import auth
# Create your views here.

class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        if not auth.already_authorized(request):
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(data=response, safe=False)
        else:
            user = auth.get_user(request)
            cities = json.loads(user.focus_cities)
            response = []
            for city in cities:
                city_temp = city.split('-')[1]
                data = get_weather(city_temp)
                data["name"] = city
                response.append(data)
            response = self.wrap_json_response(data=response,code=ReturnCode.SUCCESS)
            return JsonResponse(data=response,safe=False)

    def post(self, request):
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        # print(cities)
        response_data = []
        for city in cities:
            # print(type(city))
            # print(city.get("city"))
            data = get_weather(city.get("city"))
            data["city_info"] = city
            response_data.append(data)
        response_data = self.wrap_json_response(data=response_data)
        return JsonResponse(data=response_data, safe=False)


