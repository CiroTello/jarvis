
# * =================================================================================================================================================================
# *                     OPEN WEATHER
# * =================================================================================================================================================================
from utils.formats import *
import requests
from database.database import *

global api_weather_key

def getWeather(city, message):
    global api_weather_key

    consultWeatherKey(message)

    city = formatText(city)

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(
        city, api_weather_key
    )

    response = requests.get(url)  # GET to API

    if response.status_code == 200:
        data = response.json()  # Convert answer to JSON

        # Store the data in weather
        weather_data = {}
        weather_data["temperature"] = data["main"]["temp"]
        weather_data["humidity"] = data["main"]["humidity"]
        weather_data["pressure"] = data["main"]["pressure"]
        weather_data["wind_speed"] = data["wind"]["speed"]
        weather_data["feels_like"] = data["main"]["feels_like"]
        weather_data["city"] = data["name"]
        weather_data["country"] = data["sys"]["country"]
        weather_data["main"] = data["weather"][0]["main"]
        weather_data["description"] = data["weather"][0]["description"]
        weather_data["icon"] = data["weather"][0]["icon"]

        # Devolvemos los datos del tiempo y el clima
        return weather_data
    else:
        print("Error: ", response.status_code)
        print(response.json())

        return "Please submit your Open Weather key, or check if you sent it correctly --> /help"


def consultWeatherKey(message):
    global api_weather_key

    api_weather_key = consultarDB(message.chat.id)

    if api_weather_key is None:
        print("You don't have an openWeather key")
    else:
        api_weather_key = api_weather_key[3]
        print("Your openWeather key is: ", api_weather_key)


def actualizarWeatherKey(message):
    global api_weather_key

    message.text = formatText(message.text)

    api_weather_key = message.text

    actualizarDB_openW(message.chat.id, api_weather_key)

    return "Open weather key succesfully update"


def weatherView(data, message):
    city = data["city"]
    country = data["country"]
    temp = data["temperature"]
    feelsLike = data["feels_like"]
    humidity = data["humidity"]
    pressure = data["pressure"]
    wind_speed = data["wind_speed"]
    main = data["main"]
    description = data["description"]

    defaultConfigs = (
        "<b>========================================= J.A.R.V.I.S. 🤖</b>" + "\n" + "\n"
    )

    defaultConfigs += f"<b>🌎 El clima en {city}, {country} es:</b>" + "\n"
    defaultConfigs += f"Temperature ⋯⋯⋯⋯→ <i>{temp}°C</i>" + "\n"
    defaultConfigs += f"Feels_like ⋯⋯⋯⋯⋯→ <i>{feelsLike}°C</i>" + "\n"
    defaultConfigs += f"Humidity ⋯⋯⋯⋯⋯→ <i>{humidity}%</i>" + "\n"
    defaultConfigs += f"Pressure ⋯⋯⋯⋯⋯→ <i>{pressure}hPa</i>" + "\n"
    defaultConfigs += f"Wind_speed ⋯⋯⋯⋯→ <i>{wind_speed}miles/hour</i>" + "\n" + "\n"

    defaultConfigs += "<b>🌑 Mas info! </b>" + "\n"
    defaultConfigs += f"<b>Sky ⋯⋯⋯⋯⋯⋯⋯→  </b>{main}" + "\n"
    defaultConfigs += f"<b>Description ⋯⋯⋯→  </b>{description}" + "\n"

    icon = data["icon"]
    icono = "https://raw.githubusercontent.com/yuvraaaj/openweathermap-api-icons/master/icons/{}.png".format(
        icon
    )

    return (defaultConfigs,icono)