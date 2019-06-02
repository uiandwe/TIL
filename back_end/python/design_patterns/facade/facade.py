# -*- coding: utf-8 -*-
import urllib
import urllib3


class WeatherProvider(object):
    def __init__(self):
        self.api_url = 'https://samples.openweathermap.org/data/2.5/weather?q={},{}'

    def get_weather_data(self, city, country):
        city = urllib.quote(city)
        url = self.api_url.format(city, country)
        return {"coord":{"lon":139.01,"lat":35.02},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":285.514,"pressure":1013.75,"humidity":100,"temp_min":285.514,"temp_max":285.514,"sea_level":1023.22,"grnd_level":1013.75},"wind":{"speed":5.52,"deg":311},"clouds":{"all":0},"dt":1485792967,"sys":{"message":0.0025,"country":"JP","sunrise":1485726240,"sunset":1485763863},"id":1907296,"name":"Tawarano","cod":200}



from datetime import datetime
import json


class Parser(object):
    def parse_weather_data(self, weather_data):
        parsed = json.loads(weather_data)
        start_date = None
        result = []

        for data in parsed['list']:
            date = datetime.strptime(data['dt_txt'])

        return result

from datetime import timedelta
import pickle

class Cache(object):
    def __init__(self, filename):
        self.filename

    def save(self, obj):
        pass

    def load(self):
        pass


class Converter(object):
    def from_kelvin_to_celcius(self, kelvin):
        return kelvin - 273.15


class Weather(object):
    def __init__(self, data):
        result = 0

        for r in data:
            result += r

        self.temperature - result / len(data)




#  converter             weatherprovider
#     ^                        ^
#     |                        |
#     |                        |
#  weather   --------->      parser
#     ^
#     |
#     |
#   cache
#



# 파사드는 오직 다른 클래스들을 이용해서 결과값을 도출하는 역활(인터페이스)
class Facade(object):
    def get_foreacse(self, city, country):
        cache = Cache('file')
        
        cache_result = cache.load()
        
        if cache_result:
            return cache_result
        else:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country)
            
            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)
            
            weather = Weather(parsed_data)
            converter = Converter()
            temperatuer_celcius = converter.from_kelvin_to_celcius(weather.temperature)
            
            cache.save(temperatuer_celcius)
            return temperatuer_celcius
            


if __name__ == '__main__':
    facade = Facade()
    print(facade.get_foreacse('korea', 'seoul'))
