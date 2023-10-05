import json
import openai
import redis
import requests
 
from dotenv import load_dotenv
import os
from .data import WEATHER_TIPS

load_dotenv()

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_recommendations(data):
    """
    This function takes in weather data and returns a list of health tips based on the weather conditions.

    Args:
        data (dict): A dictionary containing weather data.

    Returns:
        list: A list of health tips.

    Raises:
        KeyError: If the required weather data is not present in the input dictionary.
    """

    # Check if OPEN_AI_API environment variable is set
    if 'OPEN_AI_API' in os.environ:
        # Get the API key from the environment variable
        open_api_key = os.environ.get('OPEN_AI_API')
        openai.api_key = open_api_key

        # Define your prompt asking for keyword suggestions
        prompt = (
            f"Provide a coma separated list of not more than 5 health tips for someone experiencing {data['weather'][0]['description']} weather with a temperature of {data['main']['temp']}°C. Separate each item with a coma only.  Use emojis to express yourself."
        )

        # Use the GPT-3 engine to get keyword suggestions
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=70,  # Adjust the number of tokens as needed
            n=5  # Specify the number of suggestions you want
        )

        weather_tips = response.choices[0].text.strip('').split(' ,')
        tips = [item.strip() for item in weather_tips[0].split(',')]

        return tips
    else:
        # If not, use WEATHER_TIPS data for recommendations
        result = {}

        # Print the weather data for debugging purposes

        tips = data['weather'][0]['id']
        
        if tips in WEATHER_TIPS:
            weather_info = WEATHER_TIPS[tips]
            result = weather_info['tips']
        
        return result



def query_location(lon, lat):
    """
    Retrieve weather information based on longitude and latitude.

    Parameters:
        lon (float): The longitude coordinate.
        lat (float): The latitude coordinate.

    Returns:
        dict: A dictionary containing weather information, or None if the request fails.
    """
    
     # Check if weather data is already stored in the cache
    cache_key = f'weather_data:{lat}:{lon}'
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return eval(cached_data)  # Convert the cached data from string to dictionary
    
    api_key = os.environ.get('WEATHER_API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"

    if lon and lat:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("cache hit")
            redis_client.setex(cache_key, 3600, str(data))  # Store the weather data in the cache
            return data

    return None


def save_location_data(data):
    """
    Update and save the location data to the Redis cache.

    Parameters:
        data (dict): A dictionary containing weather data.
    """
    redis_client.setex('locations', 3600, str(data))