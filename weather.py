import requests

API_KEY = "01090d458abaabbc8b8f92b68f09262f" #Wale: note that this is not secure. API key is stored in the code in clear text.
#Find out how to remediate this. Or is this not an issue?
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print (data)
    #print (data['weather'])
    #print (data['main']['humidity'])
    
    weather = data['weather'][0]['description']
    temperature_farheit = data['main']['temp']
    temperature_celsius = temperature_farheit - 273.15
    temperature_celsius_rounded = round(temperature_celsius, 2)
    humiditee = data['main']['humidity']

    print ("Weather:", weather)
    print ("Temperature:", temperature_celsius_rounded, "celsius")
    print ("humidity right now is", humiditee, "in", city)
else:
    print("An error occurred.")