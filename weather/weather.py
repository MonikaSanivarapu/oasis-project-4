import requests
from typing import Optional

def get_weather(api_key: str, city: str) -> None:

    if not api_key:
        raise ValueError("API key must be provided")
    if not city:
        raise ValueError("Please Provide Your City Name")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",

    }

    try:
        response = requests.get(base_url, params=params)
        data = response. json()

        if response.status_code == 200:
            # Extract relevant information from the API response
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            pressure = data["main"] ["pressure"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"] ["speed"]
            clouds = data["clouds"]["all"]
            visibility = data["visibility"]
            dew_point: Optional[float] = data.get("main", {}) .get("dew_point")
            rain: Optional[float] = data.get("rain", {}) .get("1h")

            print(f"Weather in {city}:")

            print(f"\tTemperature: {temperature}℃")

            
            print(f"\tVisibility: {visibility} m")

            print(f"\tDew Point: {dew_point}°c")

            print(f"\tPressure: {pressure} hPa")


            print(f"\tFeels Like: {feels_like}°C")
            print(f"\tMinimum Temperature: {temp_min}℃")

            print(f"\tMaximum Temperature: {temp_max}°℃")

            print(f"\tHumidity: {humidity}%")

            print(f"\tWind Speed: {wind_speed} m/s")

            print(f"\tCloud Coverage: {clouds}%")


            print(f"\tRain: {rain} mm")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error occurred: {e}")

def main() -> None:
    api_key = "6ac51341fbe25af0043f9a7e166961c4"
    city = input("Please Enter your city name or PIN code: ")

    get_weather(api_key, city)

if __name__=="__main__":
    main()