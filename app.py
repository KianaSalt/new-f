from flask import Flask, render_template, request, jsonify
import requests
import os
import asyncio
import random
import json


app = Flask(__name__)

hotels_data = [
    {"name": "Hotel A", "location": "City A"},
    {"name": "Hotel B", "location": "City B"},
    {"name": "Hotel C", "location": "City C"},
    # Add more hotel data as needed
]

# Home route
@app.route("/")                   
def home():
    return render_template("home.html")


# Booking route
@app.route("/booking")                   
def booking():
    url = 'https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation'
    querystring = {"cityName":"Berlin", "countryName":"Germany"}

    headers = {
        "X-RapidAPI-Key": "68bb373953mshbd91a0f0832fa34p15047cjsnb7984d237ebc",
        "X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }

  
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return render_template("booking.html", datum=data)

    
    
    
    
    
    
    #return response.json()
    #data = response.json()
    #print(data)
    #return render_template("booking.html", datum=data)

# Suggestions route
@app.route("/suggestions")                   
def end():

    #API
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"
    querystrings = [
     {"cityName": "Bangkok", "countryName": "Thailand"},
    {"cityName": "Punta Cana", "countryName": "Dominican Republic"},  
    ] 

    headers = {
    "X-RapidAPI-Key": "b9acad5e50msh9b9087d682ca9d9p1a812fjsnbc3e76195a9b",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }
    all_data = []

    for querystring in querystrings:
        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        all_data.append(data)

    return render_template("suggestions.html", datum=all_data)  


if __name__ == "__main__":
    app.run(debug=True)
