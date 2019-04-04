import requests
api_url="http://api.openweathermap.org/data/2.5/weather"
class CityWeather:
    def __init__(self):
        self.city=''
    def output_weather(self,city):
        params={
            'q' : city,
            'appid' : '11c0d3dc6093f7442898ee49d2430d20',
            'units' : 'metric'
        }
        result = requests.get(api_url,params=params)
        print(result.status_code)
        print(result.headers["Content-Type"])
        Qresult="Current temperature in {} is {}°C\nPressure is {} hPa\nWind speed is {} meter/sec"
        return Qresult.format(city, result.json()["main"]["temp"],result.json()["main"]["pressure"],result.json()["wind"]["speed"])

#city =''
#now=''
#now.output_weather(city)
