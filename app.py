from flask import Flask, render_template, request, redirect, url_for
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
    # visitor_ip = request.remote_addr
    visitor_ip = '125.23.44.12'

    if request.method == 'POST':
        mode = request.form.get("modeOfSearch")

        if mode == 'IP':
            request_ip = request.form.get('searchItem')
            try:
                tracked_ip = TrackIP(request_ip)
                weather = WeatherInfo(city=tracked_ip.getCity()).getWeatherByCity()
            except Exception:
                return redirect(url_for('index'))
        elif mode == 'City':
            try:
                weather = WeatherInfo(city=request.form.get('searchItem')).getWeatherByCity()
            except Exception:
                return redirect(url_for('index'))
    else:
        # Show User's weather information
        visitor_city = TrackIP(visitor_ip).getCity()
        weather = WeatherInfo(city=visitor_city).getWeatherByCity()

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)