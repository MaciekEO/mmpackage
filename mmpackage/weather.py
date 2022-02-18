from openmeteo_py import Hourly,Daily,Options,OWmanager
import datetime
import json

def greetings():
    print("Hello")
    return "Hello" 

def get_location():
    latitude = 53.1277491
    longitude = 23.0159807
    return latitude, longitude

def weather(time):
    # Latitude, Longitude for Bialystok

    latitude, longitude = get_location()

    hourly = Hourly()
    daily = Daily()
    options = Options(latitude,longitude)

    mgr = OWmanager(options,
        hourly.all(),
        #daily.sunrise()
        )

    # Download data
    meteo = mgr.get_data()

    print(f"In Bialystok at {time} we have {meteo['hourly']['soil_temperature_0cm'][time]}°C")
    print(f"Atmospheric pressure: {meteo['hourly']['pressure_msl'][time]} hPa")

    return meteo["hourly"]["soil_temperature_0cm"][time]
    # print(json.dumps(meteo, indent=4))

if __name__ == '__main__':
    now = datetime.datetime.now()
    weather(now.hour)