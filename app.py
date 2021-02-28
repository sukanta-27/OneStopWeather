from flask import Flask, render_template, request, redirect, url_for
from util.TrackIP import TrackIP
from util.WeatherInfo import WeatherInfo
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/", methods=['GET'])
def index():
    # As developing in localhost, ip will not fetch any address
    # So for testing purposes giving hardcoded random IP
    visitor_ip = request.remote_addr
    if not visitor_ip or visitor_ip == '127.0.0.1':
        return redirect(url_for('search'))
    else:
        # Show User's weather information
        visitor_city = TrackIP(visitor_ip).getCity()
        weather = WeatherInfo(city=visitor_city).getWeatherByCity()
        if weather:
            return render_template('index.html', weather=weather)
        else:
            return redirect(url_for('search'))


@app.route('/search', methods=['GET', 'POST'])
def search():
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
        elif mode == 'Zip':
            try:
                zip = request.form.get('searchItem')
                country = request.form.get('country')

                weather = WeatherInfo(zip=zip, country=country).getWeatherByZip()
            except Exception:
                return redirect(url_for('index'))

        return render_template('index.html', weather=weather)

    else:
        return render_template('search.html')
if __name__ == '__main__':
    app.run(debug=True)