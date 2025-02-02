from flask import Flask, render_template, request
from datetime import datetime
import requests
import os

app = Flask(__name__)

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

def get_icon(icon_id, response):
    image_url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
    img_data = requests.get(image_url).content
    static_folder = os.path.join('static', 'images')
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)
    image_path = os.path.join(static_folder, 'image_name.jpg')
    with open(image_path, 'wb') as handler:
        handler.write(img_data)
    return 'images/image_name.jpg'

@app.route('/',methods=['GET', 'POST'])
def index():
    weather_data = None
    sunrise = None
    sunset = None
    sunrise_formatted = None
    sunset_formatted = None
    image = None
    if request.method == 'POST':
        try:
            city_name = request.form['city']
            api_key = os.environ.get('API_KEY')
            weather_data = get_weather(city_name, api_key)
            print(weather_data)
            sunrise = weather_data['sys']['sunrise']
            sunset = weather_data['sys']['sunset']
            sunrise_formatted = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
            sunset_formatted = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')
            image = get_icon(icon_id=weather_data['weather'][0]['icon'], response=weather_data)
            # print(image)
        except Exception as e:
                error_message = f"An error occurred: {str(e)}"
    
    return render_template('index.html', weather_data=weather_data, sunrise_formatted=sunrise_formatted, sunset_formatted=sunset_formatted, image=image)    

if __name__ == "__main__":
    app.run(debug=True)
