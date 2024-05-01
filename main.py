import requests
import json


print("Welcome to Weather App.")
city = input("Enter the city name: ")

# validate user input for options
while True:
    try:
        i = int(input("What would you like to know: \n   1. The current temperatur. \n   2. The location details. \n   3. The current weather details. \nEnter the number: "))
        if i in [1,2,3]:
            break
        else:
            print("Invalidate option. Please select a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Enter your API Key
API_KEY = ""
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

try:
    r = requests.get(url)
    wDict= json.loads(r.text)
    t = (wDict["current"]["temp_c"])
    loc = (wDict["location"])
    curr = (wDict["current"])
    if i==1:
        print(f"Current temperatur of {city} is {t} °C.")
    elif i==2: 
        print(f"Location details: \n{loc}")
    elif i==3:
        print(f"Current weather: \n{curr}")
    else:
        print("Invalidate option selected.")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")