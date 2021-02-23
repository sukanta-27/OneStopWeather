from flask import Flask, render_template, request
from util.TrackIP import TrackIP
from util.WeatherInfo import WeatherInfo
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/", methods=['GET', 'POST'])
def index():
    # As developing in localhost, ip will not fetch any address
    # So for testing purposes giving hardcoded random IP
    # request_ip = request.remote_addr
    request_ip = '125.23.44.12'

    if request.method == 'POST':
        request_ip = request.form.get("searchItem")
        print(request_ip)
    city_ip = TrackIP(request_ip).getCity()
    weather = WeatherInfo(city=city_ip).getWeatherByCity()
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)