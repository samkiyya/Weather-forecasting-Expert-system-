
numerical_conditions = [
    {
        'conditions': {'Temperature': (25, float('inf')), 'Humidity': (0, 30)},
        'result': 'sunny',
        'explanation': 'The temperature is high and the humidity is low, indicating sunny weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Precipitation': (30, float('inf'))},
        'result': 'rainy',
        'explanation': 'The temperature is low and the precipitation is high, indicating rainy weather.'
    },
    {
        'conditions': {'Cloud Cover': (70, float('inf'))},
        'result': 'cloudy',
        'explanation': 'The cloud cover is high, indicating cloudy weather.'
    },
    {
        'conditions': {'Wind Speed': (10, float('inf'))},
        'result': 'windy',
        'explanation': 'The wind speed is high, indicating windy weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Wind Speed': (0, 10), 'Precipitation': (0, 10)},
        'result': 'cold',
        'explanation': 'The temperature, wind speed, and precipitation are low, indicating cold weather.'
    },
    {
        'conditions': {'Temperature': (25, float('inf')), 'Humidity': (70, float('inf')), 'Cloud Cover': (70, float('inf'))},
        'result': 'humid',
        'explanation': 'The temperature, humidity, and cloud cover are high, indicating humid weather.'
    },
    {
        'conditions': {'Precipitation': (30, float('inf')), 'Cloud Cover': (70, float('inf'))},
        'result': 'stormy',
        'explanation': 'The precipitation and cloud cover are high, indicating stormy weather.'
    },
    {
        'conditions': {'Precipitation': (0, 10), 'Cloud Cover': (0, 30)},
        'result': 'clear',
        'explanation': 'The precipitation and cloud cover are low, indicating clear weather.'
    },
    {
        'conditions': {'Wind Direction': ['N'], 'Temperature': (0, 10)},
        'result': 'northern wind',
        'explanation': 'The wind is coming from the north, indicating a northern wind.'
    },
    {
        'conditions': {'Wind Direction': ['S'], 'Temperature': (25, float('inf'))},
        'result': 'southern wind',
        'explanation': 'The wind is coming from the south, indicating a southern wind.'
    },
    {
        'conditions': {'Visibility': 'low'},
        'result': 'foggy',
        'explanation': 'The visibility is low, indicating foggy weather.'
    },
    {
        'conditions': {'Dew Point': (25, float('inf')), 'Temperature': (0, 10)},
        'result': 'dew',
        'explanation': 'The dew point is high and the temperature is low, indicating dew formation.'
    },
    {
        'conditions': {'Temperature': (25, float('inf')), 'Humidity': (30, 70), 'Wind Speed': (0, 10), 'Precipitation': (0, 10)},
        'result': 'pleasant',
        'explanation': 'The temperature is high, humidity is moderate, and wind speed and precipitation are low, indicating pleasant weather.'
    },
    {
        'conditions': {'Temperature': (25,

 float('inf')), 'Humidity': (0, 30), 'Wind Speed': (10, float('inf'))},
        'result': 'hot and windy',
        'explanation': 'The temperature is high, humidity is low, and wind speed is high, indicating hot and windy weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Humidity': (70, float('inf')), 'Precipitation': (0, 10)},
        'result': 'cool and humid',
        'explanation': 'The temperature is low, humidity is high, and precipitation is low, indicating cool and humid weather.'
    },
    {
        'conditions': {'Precipitation': (30, float('inf')), 'Cloud Cover': (0, 30)},
        'result': 'showers',
        'explanation': 'The precipitation is high and the cloud cover is low, indicating showers.'
    },
    {
        'conditions': {'Wind Direction': ['NE'], 'Wind Speed': (10, 30)},
        'result': 'northeast wind',
        'explanation': 'The wind is coming from the northeast and the wind speed is moderate, indicating a northeast wind.'
    },
    {
        'conditions': {'Wind Direction': ['SW'], 'Wind Speed': (0, 10), 'Cloud Cover': (70, float('inf'))},
        'result': 'southwest wind and cloudy',
        'explanation': 'The wind is coming from the southwest, wind speed is low, and cloud cover is high, indicating a southwest wind and cloudy weather.'
    },
    {
        'conditions': {'Visibility': 'high', 'Cloud Cover': (0, 30), 'Wind Speed': (0, 10)},
        'result': 'clear and calm',
        'explanation': 'The visibility is high, cloud cover is low, and wind speed is low, indicating clear and calm weather.'
    },
    {
        'conditions': {'Wind Speed': (10, float('inf')), 'Temperature': (25, float('inf'))},
        'result': 'strong winds',
        'explanation': 'The wind speed and temperature are high, indicating strong winds.'
    },
    {
        'conditions': {'Temperature': (25, float('inf')), 'Humidity': (0, 30), 'Cloud Cover': (0, 30)},
        'result': 'hot and clear',
        'explanation': 'The temperature is high, humidity is low, and cloud cover is low, indicating hot and clear weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Wind Speed': (10, float('inf')), 'Cloud Cover': (70, float('inf'))},
        'result': 'cold and windy',
        'explanation': 'The temperature is low, wind speed is high, and cloud cover is high, indicating cold and windy weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Humidity': (0, 30), 'Cloud Cover': (0, 30), 'Wind Speed': (0, 10)},
        'result': 'chilly',
        'explanation': 'The temperature, humidity, cloud cover, and wind speed are low, indicating chilly weather.'
    },
    {
        'conditions': {'Temperature': (25, float('inf')), 'Humidity': (70, float('inf')), 'Cloud Cover': (0, 30)},
        'result': 'warm and partly cloudy',
        'explanation': 'The temperature and humidity are high, and cloud cover is low, indicating warm and partly cloudy weather.'
    },


    {
        'conditions': {'Temperature': (10, 25), 'Wind Speed': (10, 30)},
        'result': 'moderate weather',
        'explanation': 'The temperature and wind speed are moderate, indicating moderate weather conditions.'
    },
    {
        'conditions': {'Temperature': (25, float('inf')), 'Precipitation': (0, 10)},
        'result': 'hot and dry',
        'explanation': 'The temperature is high and the precipitation is low, indicating hot and dry weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Precipitation': (70, float('inf')), 'Wind Speed': (0, 10)},
        'result': 'cold and rainy',
        'explanation': 'The temperature is low, the precipitation is high, and the wind speed is low, indicating cold and rainy weather.'
    },
    {
        'conditions': {'Temperature': (10, 25), 'Humidity': (70, float('inf')), 'Wind Speed': (0, 10)},
        'result': 'muggy',
        'explanation': 'The temperature is moderate, humidity is high, and wind speed is low, indicating muggy weather.'
    },
    {
        'conditions': {'Temperature': (0, 10), 'Humidity': (30, 70), 'Cloud Cover': (70, float('inf'))},
        'result': 'cool and overcast',
        'explanation': 'The temperature is low, humidity is moderate, and cloud cover is high, indicating cool and overcast weather.'
    },
    {
        'conditions': {'Precipitation': (30, float('inf')), 'Wind Speed': (10, float('inf'))},
        'result': 'stormy and windy',
        'explanation': 'The precipitation and wind speed are high, indicating stormy and windy weather.'
    },
    {
        'conditions': {'Wind Direction': ['N'], 'Wind Speed': (10, float('inf'))},
        'result': 'northerly gales',
        'explanation': 'The wind is coming from the north and the wind speed is high, indicating northerly gales.'
    },
    {
        'conditions': {'Wind Direction': ['S'], 'Wind Speed': (10, 30)},
        'result': 'southerly breeze',
        'explanation': 'The wind is coming from the south and the wind speed is moderate, indicating a southerly breeze.'
    },
    {
        'conditions': {'Visibility': (0, 30), 'Wind Speed': (0, 10)},
        'result': 'foggy and calm',
        'explanation': 'The visibility is low and the wind speed is low, indicating foggy and calm weather.'
    },
    {
        'conditions': {'Dew Point': (70, float('inf')), 'Temperature': (25, float('inf')), 'Humidity': (70, float('inf'))},
        'result': 'muggy and damp',
        'explanation': 'The dew point, temperature, and humidity are high, indicating muggy and damp weather.'
    },
    {
        'conditions': {'Temperature': (25, float('inf')), 'Humidity': (0, 30), 'Wind Speed': (10, float('inf'))},
        'result': 'hot and gusty',
        'explanation': 'The temperature is high, humidity is low, and wind speed is high, indicating hot and gusty weather.'
    },
 # we can Add more rules as per your requirements
 ]