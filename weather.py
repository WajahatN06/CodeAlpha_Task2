import requests 

api_key = ""    # API key from the website
web_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter your city: ")
request_url = f"{web_url}?q={city}&appid={api_key}&units=metric"  

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
else:
    print("Oops! An Error Occurred. Please check your city name and try again.")
