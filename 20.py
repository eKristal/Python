#API key - An application programming interface (API) key is a code used to identify an application or user and is used for authentication in computer applications.


import requests

# API võtme ja linna nime määramine
city = "Tallinn"
api_key = "4a18e62e5ddc75fb44404c84e809b7ca"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)
