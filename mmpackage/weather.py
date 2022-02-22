from openmeteo_py import Hourly,Options,OWmanager
import datetime
import numpy as np
import matplotlib.pyplot as plt
# import seaborn
import json

def greetings():
    print("Hello")
    return "Hello" 

def get_location(city):
    latitude = None
    longitude = None
    if city == "Białystok" or city == "Bialystok" or city == "bialystok":
        latitude = 53.1277491
        longitude = 23.0159807
    if city == "Warszawa" or city == "warszawa" or city == "Warsaw" or city == "warsaw":
        latitude = 52.2297
        longitude = 21.0122
    if city == "Berlin" or city == "berlin":
        latitude = 52.5235
        longitude = 13.4115
    if city == "Paryż" or city == "paryż" or city == "Paryz" or city == "paryz" or city == "Paris" or city == "paris":
        latitude = 48.8567
        longitude = 2.3510
    if city == "Londyn" or city == "londyn" or city == "London" or city == "london":
        latitude = 51.5002
        longitude = -0.1262
    if city == "Moskwa" or city == "moskwa" or city == "Moscow" or city == "moscow":
        latitude = 55.7558
        longitude = 37.6176
    return latitude, longitude

def get_meteo_data(latitude, longitude):
        hourly = Hourly()
        options = Options(latitude, longitude)
        mgr = OWmanager(options, hourly.all())
        return mgr.get_data()

def weather(time, cities):
    fig, ax = plt.subplots()

    for city in cities:
        latitude, longitude = get_location(city)

        meteo = get_meteo_data(latitude, longitude)
    
        print(f"In {city} at {time} we have {meteo['hourly']['soil_temperature_0cm'][time]}°C")
        print(f"Atmospheric pressure: {meteo['hourly']['pressure_msl'][time]} hPa\n")

        date = np.arange(np.datetime64(meteo['hourly']['time'][0]), np.datetime64(meteo['hourly']['time'][-1]),np.timedelta64(1, 'h'))
        temp = meteo['hourly']['soil_temperature_0cm']
        press = meteo['hourly']['pressure_msl']
        meteo['hourly']['soil_temperature_0cm'].pop()
        meteo['hourly']['pressure_msl'].pop()

        ax.plot(date, temp, label=city)

    ax.set_title("Temperature for this week", fontsize=16)
    ax.set_ylabel("Temperature [°C]")
    fig.autofmt_xdate()
    ax.legend()
    ax.grid()
    plt.show()

    return meteo["hourly"]["soil_temperature_0cm"][time]
    # print(json.dumps(meteo, indent=4))

if __name__ == '__main__':
    now = datetime.datetime.now()
    weather(now.hour, ["Warsaw", "Berlin", "Bialystok"])