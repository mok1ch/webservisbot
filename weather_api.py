import requests

class OpenWeatherApi:
    apiid = '778d5d81e3d0366e298db12584004069'

    def __init__(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.apiid}"
        self.data = eval(requests.get(url).text)

    def get_temperature(self, temp_type='K'):
        match temp_type:
            case 'K':
                return self.data['main']['temp']
            case 'C':
                return round(self.data['main']['temp'] - 273.15, 1)
            case 'F':
                return round((self.data['main']['temp'] - 273.15) * 9/5 + 32, 1)

    def get_weather(self, type_='main'):
        weather = self.data['weather'][0]
        if type_ == 'main':
            return weather['main']
        elif type_ == 'description':
            return weather['description']
        elif type_ == 'both':
            return f"{weather['main']}: {weather['description']}"


    def get_wind(self, type_='general'):
        wind_data = self.data['wind']
        if type_ == 'general':
            return wind_data['speed']
        elif type_ == 'detailed':
            direction = self.get_wind_direction(wind_data['deg']) if 'deg' in wind_data else 'N/A'
            return f"Speed: {wind_data['speed']} m/s, Gust: {wind_data.get('gust', 'N/A')} m/s, Direction: {direction}"

    @staticmethod
    def get_wind_direction(deg):
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        idx = round(deg / 45) % 8
        return directions[idx]

    def get_answer(self):
        temperature_c = self.get_temperature('C')
        weather_desc = self.get_weather('both')
        wind_info = self.get_wind('detailed')
        return f"Temperature: {temperature_c}°C, Weather: {weather_desc}, Wind: {wind_info}"

