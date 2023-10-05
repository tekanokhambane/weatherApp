from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("weather-search/", views.WeatherSearchAPIView.as_view(), name="weather_search_api"),
    path("locations/", views.LocationsAPIView.as_view(), name="locations_api"),
    path("api/location/", views.LocationAPIView.as_view(), name="weather"),
]
