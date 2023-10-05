# Weather tips for various weather conditions based on OpenWeatherMap condition codes
WEATHER_TIPS = {
    200: {
        'condition': 'Thunderstorm with Light Rain ☔⚡',
        'tips': [
            "Stay indoors and away from windows during a thunderstorm ⚡.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Listen to weather alerts for updates during the storm 📻🌩️.",
        ],
    },
    201: {
        'condition': 'Thunderstorm with Rain ☔⚡',
        'tips': [
            "Seek shelter indoors and avoid electrical appliances during a thunderstorm ⚡🏠.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Stay away from tall objects and open areas during the storm 🚫🌳.",
        ],
    },
    202: {
        'condition': 'Thunderstorm with Heavy Rain ☔⚡',
        'tips': [
            "Take cover in a sturdy building during a heavy thunderstorm ⚡🏢.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Avoid standing under trees or tall structures 🚫🌲.",
        ],
    },
    210: {
        'condition': 'Light Thunderstorm ⚡',
        'tips': [
            "Light thunderstorms are generally not severe, but stay indoors for safety 🏠.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Keep an eye on changing weather conditions 🌩️.",
        ],
    },
    211: {
        'condition': 'Thunderstorm ⚡',
        'tips': [
            "Stay indoors and away from tall objects during a thunderstorm ⚡🚫🌆.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Avoid open areas and bodies of water during the storm 🚫🏞️.",
        ],
    },
    212: {
        'condition': 'Heavy Thunderstorm ⚡',
        'tips': [
            "During a heavy thunderstorm, seek shelter indoors 🏢.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Avoid unnecessary travel during severe storms 🚗🌩️.",
        ],
    },
    221: {
        'condition': 'Ragged Thunderstorm ⚡',
        'tips': [
            "Ragged thunderstorms can bring unpredictable weather; monitor local alerts 🌩️📢.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Stay indoors and avoid outdoor activities 🏠🚫.",
        ],
    },
    230: {
        'condition': 'Thunderstorm with Light Drizzle ☔⚡',
        'tips': [
            "Stay indoors and away from water sources during a thunderstorm with light drizzle ☔🏠.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Listen to weather updates for any changes 📻🌩️.",
        ],
    },
    231: {
        'condition': 'Thunderstorm with Drizzle ☔⚡',
        'tips': [
            "During a thunderstorm with drizzle, stay indoors and avoid electrical appliances ⚡🏠.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Keep windows and doors closed to prevent water from entering 🚪🌧️.",
        ],
    },
    232: {
        'condition': 'Thunderstorm with Heavy Drizzle ☔⚡',
        'tips': [
            "Seek shelter in a sturdy building during a thunderstorm with heavy drizzle ⚡🏢.",
            "Unplug electronic devices to protect them from power surges ⚡🔌.",
            "Avoid driving in heavy rain to stay safe 🚗🌧️.",
        ],
    },
    300: {
        'condition': 'Light Drizzle ☔',
        'tips': [
            "Light drizzle may make surfaces slippery; use caution while walking or driving 🚶‍♀️🚗.",
            "Keep an umbrella handy for unexpected drizzle ☔🌂.",
        ],
    },
    301: {
        'condition': 'Drizzle ☔',
        'tips': [
            "Drizzle can reduce visibility; use headlights while driving 🚗💡.",
            "Carry an umbrella to stay dry during drizzle ☔🌂.",
        ],
    },
    302: {
        'condition': 'Heavy Drizzle ☔',
        'tips': [
            "Heavy drizzle may cause localized flooding; avoid flooded areas 🚗🌊.",
            "Drive with caution on wet roads during heavy drizzle 🚗🌧️.",
        ],
    },
    310: {
        'condition': 'Light Drizzle Rain ☔🌦️',
        'tips': [
            "Light drizzle rain can create slippery road conditions; drive carefully 🚗🌧️.",
            "Use headlights and reduce speed in light drizzle rain 🚗💡.",
        ],
    },
    311: {
        'condition': 'Drizzle Rain ☔🌦️',
        'tips': [
            "Drizzle rain may reduce visibility; use headlights and drive with caution 🚗💡.",
            "Carry an umbrella to stay dry during drizzle rain ☔🌂.",
        ],
    },
    312: {
        'condition': 'Heavy Drizzle Rain ☔🌦️',
        'tips': [
            "Heavy drizzle rain can cause flooding; avoid driving through flooded areas 🚗🌊.",
            "Use caution while driving on wet roads during heavy drizzle rain 🚗🌧️.",
        ],
    },
    313: {
        'condition': 'Shower Rain and Drizzle ☔🌦️',
        'tips': [
            "Shower rain and drizzle can make roads slippery; drive with care 🚗🌧️.",
            "Carry an umbrella to stay dry during shower rain and drizzle ☔🌂.",
        ],
    },
    314: {
        'condition': 'Heavy Shower Rain and Drizzle ☔🌦️',
        'tips': [
            "Heavy shower rain and drizzle may lead to flooding; avoid flooded areas 🚗🌊.",
            "Drive with extreme caution on wet roads during heavy shower rain and drizzle 🚗🌧️.",
        ],
    },
    321: {
        'condition': 'Shower Drizzle ☔🌦️',
        'tips': [
            "Shower drizzle may create hazardous road conditions; drive safely 🚗🌧️.",
            "Carry an umbrella to stay dry during shower drizzle ☔🌂.",
        ],
    },
    500: {
        'condition': 'Light Rain ☔',
        'tips': [
            "Light rain can make roads slippery; drive carefully and maintain a safe following distance 🚗🌧️.",
            "Carry an umbrella to stay dry during light rain ☔🌂.",
        ],
    },
    501: {
        'condition': 'Moderate Rain ☔',
        'tips': [
            "Moderate rain may reduce visibility; use headlights and drive with caution 🚗💡.",
            "Carry an umbrella and raincoat to stay dry during moderate rain ☔🌂.",
        ],
    },
    502: {
        'condition': 'Heavy Rain ☔',
        'tips': [
            "Heavy rain can lead to flooding; avoid driving through flooded areas 🚗🌊.",
            "Stay indoors during heavy rain to stay dry and safe 🏠☔.",
        ],
    },
    503: {
        'condition': 'Very Heavy Rain ☔',
        'tips': [
            "Very heavy rain can cause severe flooding; stay indoors and monitor local alerts 🏠🌊.",
            "Do not drive through flooded roads during very heavy rain 🚗🌊.",
        ],
    },
    504: {
        'condition': 'Extreme Rain ☔',
        'tips': [
            "Extreme rain is dangerous; seek high ground and stay indoors 🏠⚠️.",
            "Do not attempt to drive during extreme rain 🚗🌊.",
        ],
    },
    511: {
        'condition': 'Freezing Rain ❄️☔',
        'tips': [
            "Freezing rain can create icy conditions; use caution while walking or driving 🚶‍♀️🚗.",
            "Avoid driving in freezing rain if possible 🚗❄️.",
        ],
    },
    520: {
        'condition': 'Light Shower Rain ☔🌦️',
        'tips': [
            "Light shower rain can make roads slippery; drive carefully 🚗🌧️.",
            "Carry an umbrella to stay dry during light shower rain ☔🌂.",
        ],
    },
    521: {
        'condition': 'Shower Rain ☔🌦️',
        'tips': [
            "Shower rain may reduce visibility; use headlights and drive with caution 🚗💡.",
            "Carry an umbrella and raincoat to stay dry during shower rain ☔🌂.",
        ],
    },
    522: {
        'condition': 'Heavy Shower Rain ☔🌦️',
        'tips': [
            "Heavy shower rain can lead to localized flooding; avoid flooded areas 🚗🌊.",
            "Stay indoors during heavy shower rain to stay dry and safe 🏠☔.",
        ],
    },
    531: {
        'condition': 'Ragged Shower Rain ☔🌦️',
        'tips': [
            "Ragged shower rain can bring unpredictable weather; monitor local alerts 🌩️📢.",
            "Avoid driving through flooded roads during ragged shower rain 🚗🌊.",
        ],
    },
    600: {
        'condition': 'Light Snow ❄️',
        'tips': [
            "Light snow may create slippery roads; use caution while driving 🚗❄️.",
            "Dress warmly in layers to stay comfortable in light snow ❄️🧥.",
        ],
    },
    601: {
        'condition': 'Snow ❄️',
        'tips': [
            "Snow can reduce visibility and create hazardous driving conditions 🚗❄️.",
            "Drive slowly and maintain a safe following distance in snowy conditions 🚗🌨️.",
        ],
    },
    602: {
        'condition': 'Heavy Snow ❄️',
        'tips': [
            "Heavy snow can lead to road closures and dangerous conditions; stay home if possible 🚗❄️🏡.",
            "If you must drive, use snow chains and drive with extreme caution 🚗⛓️.",
        ],
    },
    611: {
        'condition': 'Sleet ❄️',
        'tips': [
            "Sleet can create icy surfaces; walk and drive carefully 🚶‍♀️🚗.",
            "Use caution on icy roads during sleet conditions 🚗❄️.",
        ],
    },
    612: {
        'condition': 'Shower Sleet ❄️',
        'tips': [
            "Shower sleet can create hazardous road conditions; drive with care 🚗❄️🌧️.",
            "Use caution on icy roads during shower sleet 🚗❄️.",
        ],
    },
    615: {
        'condition': 'Light Rain and Snow ❄️☔',
        'tips': [
            "Light rain and snow may make roads slippery; drive carefully 🚗🌧️❄️.",
            "Dress warmly in layers to stay comfortable in mixed rain and snow ❄️🧥🌂.",
        ],
    },
    616: {
        'condition': 'Rain and Snow ❄️☔',
        'tips': [
            "Rain and snow can reduce visibility; use headlights and drive with caution 🚗💡❄️.",
            "Carry an umbrella and dress warmly in mixed rain and snow conditions ☔🧥❄️.",
        ],
    },
    620: {
        'condition': 'Light Shower Snow ❄️🌦️',
        'tips': [
            "Light shower snow can create slippery roads; drive carefully 🚗❄️🌧️.",
            "Dress warmly in layers to stay comfortable during light shower snow ❄️🧥.",
        ],
    },
    621: {
        'condition': 'Shower Snow ❄️🌦️',
        'tips': [
            "Shower snow may reduce visibility; use headlights and drive with caution 🚗💡❄️.",
            "Carry an umbrella and dress warmly in mixed rain and snow conditions ☔🧥❄️.",
        ],
    },
    622: {
        'condition': 'Heavy Shower Snow ❄️🌦️',
        'tips': [
            "Heavy shower snow can lead to hazardous road conditions; avoid unnecessary travel 🚗❄️🌧️.",
            "Stay indoors during heavy shower snow to stay warm and safe 🏠❄️.",
        ],
    },
    701: {
        'condition': 'Mist 🌫️',
        'tips': [
            "Mist can reduce visibility; use low beams while driving 🚗💡.",
            "Drive with caution and be prepared for reduced visibility in misty conditions 🚗🌫️.",
        ],
    },
    711: {
        'condition': 'Smoke 🌫️',
        'tips': [
            "Smoke can reduce air quality; stay indoors and keep windows closed 🏠🚫🌬️.",
            "Use air purifiers to improve indoor air quality during smoky conditions 🏠🌬️.",
        ],
    },
    721: {
        'condition': 'Haze 🌫️',
        'tips': [
            "Haze may reduce visibility; drive with caution and use headlights 🚗💡.",
            "Limit outdoor activities in hazy conditions to protect your health 🚫🌫️.",
        ],
    },
    731: {
        'condition': 'Sand/Dust Whirls 🌪️',
        'tips': [
            "Sand and dust whirls can reduce visibility; avoid driving in dusty conditions if possible 🚗🌪️.",
            "Protect your eyes and respiratory system from airborne particles 🏜️😷.",
        ],
    },
    741: {
        'condition': 'Fog 🌫️',
        'tips': [
            "Fog can greatly reduce visibility; use low beams while driving and maintain a safe following distance 🚗💡.",
            "Drive slowly and cautiously in foggy conditions to stay safe 🚗🌫️.",
        ],
    },
    751: {
        'condition': 'Sand 🏜️',
        'tips': [
            "Sandstorms can create hazardous driving conditions; avoid driving in sandstorms 🚗🏜️.",
            "Protect your eyes, nose, and mouth from blowing sand 🤧🌬️.",
        ],
    },
    761: {
        'condition': 'Dust 🏜️',
        'tips': [
            "Dusty conditions can reduce visibility; avoid unnecessary outdoor activities 🚫🏜️.",
            "Use protective masks to shield your respiratory system from dust particles 😷🌬️.",
        ],
    },
    762: {
        'condition': 'Volcanic Ash 🌋',
        'tips': [
            "During a volcanic ash event, stay indoors and keep windows and doors closed 🏠🚫🌋.",
            "Use air purifiers to filter out volcanic ash particles from indoor air 🌬️🏠.",
        ],
    },
    771: {
        'condition': 'Squalls 💨',
        'tips': [
            "Squalls can create sudden strong winds; secure outdoor objects and take shelter 🌬️🏠.",
            "Avoid being near the coast or on the water during squalls 🚫⛵.",
        ],
    },
    781: {
        'condition': 'Tornado 🌪️',
        'tips': [
            "During a tornado, seek shelter in a sturdy building or basement 🏠⚠️.",
            "Stay away from windows and protect yourself from flying debris 🪨🌪️.",
        ],
    },
    800: {
        'condition': 'Clear Sky ☀️',
        'tips': [
            "Enjoy the clear sky and sunny weather ☀️😎.",
            "Wear sunscreen to protect your skin from harmful UV rays ☀️🧴.",
        ],
    },
    801: {
        'condition': 'Few Clouds 🌤️',
        'tips': [
            "Partly cloudy skies make for pleasant outdoor conditions 🌤️🌳.",
            "Stay hydrated and wear sunglasses to shield your eyes from the sun 🕶️🥤.",
        ],
    },
    802: {
        'condition': 'Scattered Clouds 🌥️',
        'tips': [
            "Scattered clouds provide a mix of sun and shade 🌥️🌞.",
            "Enjoy outdoor activities while the weather is pleasant 🌳😃.",
        ],
    },
    803: {
        'condition': 'Broken Clouds 🌥️',
        'tips': [
            "Broken clouds create variable sky conditions 🌥️⛅.",
            "Carry an umbrella in case of passing showers ☔🌂.",
        ],
    },
    804: {
        'condition': 'Overcast Clouds ☁️',
        'tips': [
            "Overcast skies may bring gloomy weather; prepare for possible rain ☁️🌧️.",
            "Bring an umbrella and wear appropriate clothing for overcast conditions ☔🧥.",
        ],
    },
}

