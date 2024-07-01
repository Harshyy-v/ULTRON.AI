import requests
from bs4 import BeautifulSoup
from func.Speak import speak

def scrape_weather():
    city = "hisar"
    try:
        url = f"https://www.google.com/search?q=weather+{city}"
        # Fetch HTML content
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            temp_element = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
            temp = temp_element.text.strip() if temp_element else "Temperature data not found"
            str_element = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
            if str_element:
                data = str_element.text.split('\n')
                time = data[0]
                sky = data[1]
            else:
                time = "Time data not found"
                sky = "Sky data not found"

            # Find other weather data
            other_data_element = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')
            if other_data_element:
                other_data = other_data_element.text
                pos = other_data.find('Wind')
                other_data = other_data[pos:].strip() if pos != -1 else "Wind data not found"
            else:
                other_data = "Other weather data not found"

            # Print weather information
            print("Temperature:", temp)
            print("Time:", time)
            print("Sky Description:", sky)
            speak("Temperature is:", temp)
            speak("Sky is:", sky)
            # print("Other Weather Data:", other_data)

        else:
            print(f"Error: Failed to fetch the page. Status code: {response.status_code}")

    except Exception as e:
        print("An error occurred:", e)








# import requests
# import json
#
# # Replace with your own API key
# api_key = "70bc2fc0a58f342db988d10b17de92c1"
#
# # Prompt the user to enter the city name
# city_name = input("Enter the city name: ")
#
# # Construct the API endpoint URL
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
#
# # Make the API request
# response = requests.get(url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Get the weather data from the response
#     weather_data = response.json()
#
#     # Extract the relevant information
#     city = weather_data["name"]
#     temperature = weather_data["main"]["temp"]
#     description = weather_data["weather"][0]["description"]
#     wind_speed = weather_data["wind"]["speed"]
#     humidity = weather_data["main"]["humidity"]

    # Print the weather information
#     print(f"The weather in {city} is {description} with a temperature of {temperature}°C.")
#     print(f"Wind speed: {wind_speed} m/s")
#     print(f"Humidity: {humidity}%")
# else:
#     print(f"Error: {response.status_code}")














# enter city name
# city = "lucknow"
#
# # creating url and requests instance
# url = "https://www.google.com/search?q="+"weather"+city
# html = requests.get(url).content
#
# # getting raw data
# soup = BeautifulSoup(html, 'html.parser')
# temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
# str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
#
# # formatting data
# data = str.split('\n')
# time = data[0]
# sky = data[1]
#
# # getting all div tag
# listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
# strd = listdiv[5].text
#
# # getting other required data
# pos = strd.find('Wind')
# other_data = strd[pos:]
#
# # printing all data
# print("Temperature is", temp)
# print("Time: ", time)
# print("Sky Description: ", sky)
# print(other_data)

















