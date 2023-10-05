import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import openai
import redis
import datetime
from django.views.generic import View
from django.contrib.gis.geos import Point
from ipware import get_client_ip
from .data import WEATHER_TIPS
from .utils import get_recommendations, query_location, save_location_data
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to Redis (replace with your Redis server information)
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)


import requests


def home(request):
    client_ip, is_routable = get_client_ip(request)
    locations = []

    my_locations = redis_client.get("locations")
    if my_locations:
        locations = eval(my_locations)

    if client_ip:
        response = requests.get(f"https://ipinfo.io/{client_ip}/json")
        if response.status_code == 200:
            location_info = response.json()

            if "loc" in location_info:
                latitude, longitude = location_info["loc"].split(",")
                data = query_location(longitude, latitude)
                weather_tips = get_recommendations(data)

                return render(request, "weatherapp/index.html", {
                    "data": data,
                    "weather_tips": weather_tips,
                    "locations": locations,
                })

    return render(request, "weatherapp/index.html", {"locations": locations})


def get_weather(request):
    client_ip, is_routable = get_client_ip(request)
    my_locations = redis_client.get("locations")
    locations = eval(my_locations) if my_locations else []

    if client_ip:
        response = requests.get(f"https://ipinfo.io/{client_ip}/json")
        if response.status_code == 200:
            location_info = response.json()
            if "loc" in location_info:
                latitude, longitude = location_info["loc"].split(",")
                data = query_location(longitude, latitude)
                weather_tips = get_recommendations(data)
                return render(request, "weatherapp/index.html", {
                    "data": data,
                    "weather_tips": weather_tips,
                    "locations": locations,
                })

    return render(request, "weatherapp/index.html", {"locations": locations})


class LocationsAPIView(View):
    def get(self, request):
        # Retrieve saved locations from Redis
        saved_locations = redis_client.get("locations")

        # Convert saved locations from bytes to string
        locations_str = saved_locations.decode() if saved_locations else ""

        # Convert locations string to list
        locations = eval(locations_str) if locations_str else []

        # Return the locations as a JSON response
        return JsonResponse({"locations": locations})


class WeatherSearchAPIView(View):
    def get(self, request):
        """
        Retrieves city data from the given request.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: A JSON response containing the city data or an error message.
        """
        # Retrieve the city from the request parameters
        city = request.GET.get("city")

        # Retrieve the saved locations from Redis
        saved_locations = redis_client.get("locations")
        locations = eval(saved_locations) if saved_locations else []

        # Find the city data in the saved locations
        city_data = next((location["data"] for location in locations if location["city"] == city), None)

        # Return the city data if found, otherwise return an error message
        return JsonResponse({"city_data": city_data}) if city_data else JsonResponse({"error": f"No data found for city: {city}"})



    def post(self, request, *args, **kwargs):
        city_qs = request.POST.get("city")
        city = str(city_qs).lower()
        units = request.POST.get("units")
        temp_unit = "C" if units == "metric" else "F"

        api_key = os.environ.get("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]
            weather_tips = get_recommendations(data)

            city_data = {
                "moment": datetime.datetime.now(),
                "temperature": temperature,
                "description": description,
                "icon": icon,
                "unit": temp_unit,
                "weather_tips": weather_tips,
            }

            city_info = {"city": city, "data": []}
            saved_locations = redis_client.get("locations")
            locations = eval(saved_locations) if saved_locations else []

            if locations and len(locations) > 0:
                for location in locations:
                    if location["city"] == city:
                        location["data"].append(city_data)
                        save_location_data(locations)
                        break
                else:
                    city_info["data"].append(city_data)
                    locations.append(city_info)
                    save_location_data(locations)
            else:
                city_info = {"city": city, "data": [city_data]}
                locations.append(city_info)
                save_location_data(locations)

            context = {
                "city": city,
                "unit": temp_unit,
                "temperature": temperature,
                "description": description,
                "city_data": city_data,
                "icon": icon,
                "weather_tips": weather_tips,
                "confirmation": "City and recommendation saved successfully",
            }

            return JsonResponse({"data": context})
        else:
            context = {"error": "Error fetching weather data"}
            return JsonResponse(context)


class LocationAPIView(View):
    def get(self, request):
        city = request.GET.get("city")
        saved_locations = redis_client.get("locations")
        locations = eval(saved_locations) if saved_locations else []

        # Filter the city
        my_location = [location for location in locations if location["city"] == city]

        # Return the location data as JSON response
        return JsonResponse({"data": my_location})
