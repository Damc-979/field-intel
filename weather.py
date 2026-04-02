import requests, re
k=1
g=1
print ("Hi welcome to weather querry", "\n\n-Type in the name of your town-\n")

        

weather_codes = {
0: "Clear sky 😊",
1: "Mainly clear 😊",
2: "Partly cloudy 🌤",
3: "Overcast ☁️",
45: "Foggy 🌫️",
48: "Icy fog 🌫️🌫️",
51: "Light drizzle 🌦️",
53: "Moderate drizzle 🌦️",
55: "Dense intensity drizzle",
61: "Light rain 🌧️",
63: "Moderate Rain 🌧️  ",
65: "Heavy rain 🌧️ ",
71: "Light snow 🌨️",
73: " Moderatte snow 🌨️ ",
75: "Heavy snow 🌨️ ",
77: "Snow grains 🌨️ ",
80: "Rain showers, slight 🌧️ ",
81: "Moderate rain showers 🌧️",
82: "Violent rain showers 🌧️",
85: "SLight snow showers 🌨️ ",
86: "Heavy snow showers 🌨️🌨️",
95: "Thunderstorm ⛈️⚡️⛈️",
96: "Thanderstorm with slight hail ⛈️-🌨️",
99: "Thunderstorm heavy hail ⛈️⛈️-🌨️🌨️   "
     }



while True:
    
    name = input("Name of Your town is:").strip().lower()
    if not re.match(r'^[a-zA-ZÀ-ÿ0-9\s\-]+$', name):
        print("Please enter a valid city name using letters only.")
        g=g+1
        if g >10:
         break
        continue
    
    url= "https://geocoding-api.open-meteo.com/v1/search"
    
    params = {
            "name": name,
            "count": 1,
            
            }
    response = requests.get(url, params=params)
            
    data_1 = response.json()
    if "results" not in data_1:
        print("City not found. Please try again.")
        g=g+1
        if g >10:
         break

        continue
    else:
          l = data_1["results"][0]["latitude"]
          lo = data_1["results"][0]["longitude"]
            
            
            
          url="https://api.open-meteo.com/v1/forecast"
    
    
          params = {
                "latitude": l,
                "longitude": lo,
                 "current_weather": True
                }
       
                
    response = requests.get(url, params=params)
    data = response.json()
    a = data["current_weather"]["weathercode"]
    print("\nTemperature in ", name,":", data["current_weather"]["temperature"], "°C")
    print("\nWind speed:", data["current_weather"]["windspeed"], "km/h")
    print("\nWeather condition:", data["current_weather"]["weathercode"])
        
    print(weather_codes.get(a, "\nUnknown condition"))
    
    print("\nWhat is your next location of interest?🎯\n")
    
    k=k+1
    if k>5:
         print("That was your 5th City, try again tomorow.")
         break
    else: 
     
     continue

    
