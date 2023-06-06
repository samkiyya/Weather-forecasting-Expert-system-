categorical_conditions = [
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'low'},
        'result': 'sunny',
        'explanation': 'The temperature is high and the humidity is low, indicating sunny weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Precipitation': 'high'},
        'result': 'rainy',
        'explanation': 'The temperature is low and the precipitation is high, indicating rainy weather.'
    },
    {
        'conditions': {'Cloud Cover': 'high'},
        'result': 'cloudy',
        'explanation': 'The cloud cover is high, indicating cloudy weather.'
    },
    {
        'conditions': {'Wind Speed': 'high'},
        'result': 'windy',
        'explanation': 'The wind speed is high, indicating windy weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Wind Speed': 'low', 'Precipitation': 'low'},
        'result': 'cold',
        'explanation': 'The temperature, wind speed, and precipitation are low, indicating cold weather.'
    },
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'high', 'Cloud Cover': 'high'},
        'result': 'humid',
        'explanation': 'The temperature, humidity, and cloud cover are high, indicating humid weather.'
    },
    {
        'conditions': {'Precipitation': 'high', 'Cloud Cover': 'high'},
        'result': 'stormy',
        'explanation': 'The precipitation and cloud cover are high, indicating stormy weather.'
    },
    {
        'conditions': {'Precipitation': 'low', 'Cloud Cover': 'low'},
        'result': 'clear',
        'explanation': 'The precipitation and cloud cover are low, indicating clear weather.'
    },
    {
        'conditions': {'Wind Direction': 'N', 'Temperature': 'low'},
        'result': 'northern wind',
        'explanation': 'The wind is coming from the north, indicating a northern wind.'
    },
    {
        'conditions': {'Wind Direction': 'S', 'Temperature': 'high'},
        'result': 'southern wind',
        'explanation': 'The wind is coming from the south, indicating a southern wind.'
    },
    {
        'conditions': {'Visibility': 'low'},
        'result': 'foggy',
        'explanation': 'The visibility is low, indicating foggy weather.'
    },
    {
        'conditions': {'Dew Point': 'high', 'Temperature': 'low'},
        'result': 'dew',
        'explanation': 'The dew point is high and the temperature is low, indicating dew formation.'
    },
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'moderate', 'Wind Speed': 'low', 'Precipitation': 'low'},
        'result': 'pleasant',
        'explanation': 'The temperature is high, humidity is moderate, and wind speed and precipitation are low, indicating pleasant weather.'
    },
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'low', 'Wind Speed': 'high'},
        'result': 'hot and windy',
        'explanation': 'The temperature is high, humidity is low, and wind speed is high, indicating hot and windy weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Humidity': 'high', 'Precipitation': 'low'},
        'result': 'cool and humid',
        'explanation': 'The temperature is low, humidity is high, and precipitation is low, indicating cool and humid weather.'
    },
    {
        'conditions': {'Precipitation': 'high', 'Cloud Cover': 'low'},
        'result': 'showers',
        'explanation': 'The precipitation is high and the cloud cover is low, indicating showers.'
    },
    {
        'conditions': {'Wind Direction': 'NE', 'Wind Speed': 'moderate'},
        'result': 'northeast wind',
        'explanation': 'The wind is coming from the northeast and the wind speed is moderate, indicating a northeast wind.'
    },
    {
        'conditions': {'Wind Direction': 'SW', 'Wind Speed': 'low', 'Cloud Cover': 'high'},
        'result': 'southwest wind and cloudy',
        'explanation': 'The wind is coming from the southwest, wind speed is low, and cloud cover is high, indicating a southwest wind and cloudy weather.'
    },
    {
        'conditions': {'Visibility': 'high', 'Cloud Cover': 'low', 'Wind Speed': 'low'},
        'result': 'clear and calm',
        'explanation': 'The visibility is high, cloud cover is low, and wind speed is low, indicating clear and calm weather.'
    },
    {
        'conditions': {'Wind Speed': 'high', 'Temperature': 'high'},
        'result': 'strong winds',
        'explanation': 'The wind speed and temperature are high, indicating strong winds.'
    },
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'low', 'Cloud Cover': 'low'},
        'result': 'hot and clear',
        'explanation': 'The temperature is high, humidity is low, and cloud cover is low, indicating hot and clear weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Wind Speed': 'high', 'Cloud Cover': 'high'},
        'result': 'cold and windy',
        'explanation': 'The temperature is low, wind speed is high, and cloud cover is high, indicating cold and windy weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Humidity': 'low', 'Cloud Cover': 'low', 'Wind Speed': 'low'},
        'result': 'chilly',
        'explanation': 'The temperature, humidity, cloud cover, and wind speed are low, indicating chilly weather.'
    },
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'high', 'Cloud Cover': 'low'},
        'result': 'warm and partly cloudy',
        'explanation': 'The temperature and humidity are high, and cloud cover is low, indicating warm and partly cloudy weather.'
    },
    {
        'conditions': {'Temperature': 'moderate', 'Wind Speed': 'moderate'},
        'result': 'moderate weather',
        'explanation': 'The temperature and wind speed are moderate, indicating moderate weather conditions.'
    },
    {
        'conditions': {'Temperature': 'high', 'Precipitation': 'low'},
        'result': 'hot and dry',
        'explanation': 'The temperature is high and the precipitation is low, indicating hot and dry weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Precipitation': 'high', 'Wind Speed': 'low'},
        'result': 'cold and rainy',
        'explanation': 'The temperature is low, the precipitation is high, and the wind speed is low, indicating cold and rainy weather.'
    },
    {
        'conditions': {'Temperature': 'moderate', 'Humidity': 'high', 'Wind Speed': 'low'},
        'result': 'muggy',
        'explanation': 'The temperature is moderate, humidity is high, and wind speed is low, indicating muggy weather.'
    },
    {
        'conditions': {'Temperature': 'low', 'Humidity': 'moderate', 'Cloud Cover': 'high'},
        'result': 'cool and overcast',
        'explanation': 'The temperature is low, humidity is moderate, and cloud cover is high, indicating cool and overcast weather.'
    },
    {
        'conditions': {'Precipitation': 'high', 'Wind Speed': 'high'},
        'result': 'stormy and windy',
        'explanation': 'The precipitation and wind speed are high, indicating stormy and windy weather.'
    },
    {
        'conditions': {'Wind Direction': 'N', 'Wind Speed': 'high'},
        'result': 'northerly gales',
        'explanation': 'The wind is coming from the north and the wind speed is high, indicating northerly gales.'
    },
    {
        'conditions': {'Wind Direction': 'S', 'Wind Speed': 'moderate'},
        'result': 'southerly breeze',
        'explanation': 'The wind is coming from the south and the wind speed is moderate, indicating a southerly breeze.'
    },
    {
        'conditions': {'Visibility': 'low', 'Wind Speed': 'low'},
        'result': 'foggy and calm',
        'explanation': 'The visibility is low and the wind speed is low, indicating foggy and calm weather.'
    },
    {
        'conditions': {'Dew Point': 'high', 'Temperature': 'high', 'Humidity': 'high'},
        'result': 'muggy and damp',
        'explanation': 'The dew point, temperature, and humidity are high, indicating muggy and damp weather.'
    },
    {
        'conditions': {'Temperature': 'high', 'Humidity': 'low', 'Wind Speed': 'high'},
        'result': 'hot and gusty',
        'explanation': 'The temperature is high, humidity is low, and wind speed is high, indicating hot and gusty weather.'
    },
    # we can Add more rules as per your requirements
]
