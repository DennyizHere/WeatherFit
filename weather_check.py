import requests
import os
import sys

def weather_check(lat, long):
    with open(os.path.join(sys.path[0], "secret"), "r") as f:
        key = f.read()
    url = "https://api.darksky.net/forecast/" + key +"/" + lat + "," + long
    r = requests.get(url)
    weather = r.json()
    return (weather['currently']['summary'], weather['currently']['temperature'])

if __name__ == '__main__':
    current_conditions = weather_check("37.550201","-121.980827")
    print (current_conditions)