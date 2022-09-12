import requests, json

from twilio.rest import Client
from time import sleep

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name CITY = "Hyderabad"
# API key API_KEY = "Your API Key"
# upadting the URL
URL = BASE_URL + "q=" + "Ottawa" + "&appid=" + "d286bed21f3061725aedabbaf33428ff"
# HTTP request




# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client('ACa67fbc986c7c6fed45ba2bb497ba2239','8b82bd442ce36fd87a9fa11651da2231')
while True:
    response = requests.get(URL)
    data = response.json()
    temp_in_celsius=round(data["main"]["temp"]-273.15,2)
    print(temp_in_celsius,data["main"]["temp"])

    
    message = client.messages.create(
                                body="Temp in Ottawa : "+str(temp_in_celsius)+" C°",
                                from_='+16139020695',
                                to='+1(613) 795-5851'
                            )
    sleep(3600)
    print(message.sid)





