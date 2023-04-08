import requests
from twilio.rest import Client

"""
Four functions we'll need: 
#1: call weather service to get weather data - DONE
#2: Get weather data and create string from the data acquired-DONE
#3: Use the string just created and send message using Twilio - DONE
#4: Ties all three together - DONE
"""

def get_weather_data() -> dict:
    appid = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?zip=78620,US&appid={appid}&units=imperial"
    r = requests.get(url)
    return r.json()

def create_message_from_data(weather_data: dict) -> str:
    current_temp = weather_data["main"]["temp"]
    wind_speed = weather_data["wind"]["speed"]

    message = f"Good morning! The current temp is {current_temp}ºF and the wind is {wind_speed} mph!"
    if current_temp <= 50:
        message += " Should start car - it's going to be chilly!!"
    
    return message

def send_weather_message(message: str) -> None:
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_='',
        to=''
    )

def main():
    data = get_weather_data()
    message = create_message_from_data(data)
    send_weather_message(message)

main()
