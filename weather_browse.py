from googletrans import Translator
import requests

def get_weather_report():
    def get_weather(api_key, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_info = {
                'Location': data['name'],
                'Temperature': data['main']['temp'],
                'Condition': data['weather'][0]['description'],
                'Humidity': data['main']['humidity'],
                'Wind Speed': data['wind']['speed'],
                'Wind Direction': data['wind']['deg'],
                'Visibility': data['visibility'] / 1000
            }
            return weather_info
        else:
            print("Failed to fetch weather data. Error:", response.status_code)
            return None

    def translate_to_nepali(text):
        try:
            translator = Translator()
            translation = translator.translate(text, dest='ne').text
            return translation
        except Exception as e:
            print("Translation error:", e)
            return text

    api_key = 'df1eeea1f46f844b92291f4c88c03641'
    city = 'Kathmandu'
    weather_info = get_weather(api_key, city)
    if weather_info:
        weather_report = (
            f"{city} को मौसम को स्थिति एस्तो रहेको छ। "
            f"तापमान: {weather_info['Temperature']} °C, "
            f"स्थिति: {translate_to_nepali(weather_info['Condition'])}, "
            f"चिस्यान: {weather_info['Humidity']}, "
            f"हावाको गति: {weather_info['Wind Speed']} m/s, "
            f"हावाको दिशा: {weather_info['Wind Direction']}°, "
            f"दृश्यता: {weather_info['Visibility']} km"
        )
        return weather_report
    else:
        return "Weather information could not be retrieved."