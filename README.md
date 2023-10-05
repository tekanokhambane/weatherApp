# Weather App

The Weather App is a Django-based web application that allows users to retrieve weather information for a specific city. It utilizes the OpenWeatherMap API to fetch real-time weather data and provides personalized recommendations based on the weather conditions. The application also leverages OpenAI's natural language processing capabilities to generate weather tips for users.

## Business Logic

### Retrieving Weather Data
- The user submits a request specifying the city and preferred units (metric or imperial) through a POST request to the server.
- The server receives the request and extracts the city and units from the request parameters.
- The server retrieves the OpenWeatherMap API key from the environment variable.
- Using the city and units information, the server constructs the API request URL.
- The server sends a GET request to the OpenWeatherMap API with the constructed URL.
- The server receives the response from the API.

### Processing Weather Data
- If the API response status code is 200 (indicating a successful request), the server parses the response JSON to extract the necessary weather data.
- The server retrieves the temperature, description, and icon from the parsed JSON data.
- The server generates a timestamp for the current moment.
- The server determines the temperature unit based on the user's preferred units.
- The server calls the `get_recommendations()` function, passing the parsed JSON data, to generate personalized weather recommendations using OpenAI's natural language processing capabilities.
- The server prepares a dictionary containing the weather data, including the moment, temperature, description, icon, unit, and weather recommendations.

### Handling Saved Locations
- The server retrieves the saved locations from a Redis database.
- If there are saved locations, the server checks if the requested city already exists in the saved locations.
- If the city exists, the server appends the current weather data to the existing city data and saves the updated information back to the Redis database.
- If the city does not exist, the server creates a new entry for the city and saves the weather data.
- If there are no saved locations, the server creates a new entry for the city and saves the weather data.

### Generating Response
- The server prepares a response context dictionary containing the city, temperature unit, temperature, description, icon, weather recommendations, and a confirmation message.
- The server returns a JSON response containing the response context.

#### Note: Use Case without OpenWeatherMap API Key
If the OpenWeatherMap API key is not available, the Weather App will not be able to fetch real-time weather data. However, the application will still be able to provide other functionalities such as saving user preferences, generating random weather recommendations, and displaying previously saved weather data for cities.

## Personalized Recommendations

The Weather App generates personalized recommendations based on the weather data received from the OpenWeatherMap API and utilizes OpenAI's natural language processing capabilities. The `get_recommendations()` function takes the parsed JSON data as input and generates recommendations based on the weather conditions. Note that if the OpenAI API key is not available in your environment variables, the function use the localy saved weather tips.

The personalized recommendations aim to provide useful information and suggestions to the user based on the current weather conditions, ensuring a better user experience and preparedness for the weather.

