#!/usr/local/bin/python3

from flask import Flask, render_template, redirect, request
import requests
import json

def api_res(city):
    api_key = "762af920b22847edbd5220435212005"
    City = city
    url = "http://api.weatherapi.com/v1/current.json?key="+api_key+"&q=+"+City
    response = requests.get(url)

    data = response.text
    parsed = json.loads(data)
    return parsed

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        city = request.form["city"]
        data = api_res(city)
        try:
            return render_template("index.html", country = data["location"]["country"], temp_f = data["current"]["temp_f"], icon  = data["current"]["condition"]["icon"], wind =data["current"]["wind_mph"] , city = data["location"]["name"], region = data["location"]["region"])
        except:
            return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
    
    
