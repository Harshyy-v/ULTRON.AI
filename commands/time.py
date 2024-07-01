import requests
from bs4 import BeautifulSoup
from func.Speak import speak

def fetch_time():
    city = "Gurugram"
    try:
        # Create URL
        url = f"https://www.google.com/search?q=weather+{city}"

        # Fetch HTML content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find time
            time_element = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
            time_data = time_element.text.strip().split('\n')[0] if time_element else "Time data not found"

            # Print time
            print("ULTRON:", time_data)
            speak(f"The time is : {time_data}")

        else:
            print(f"Error: Failed to fetch the page. Status code: {response.status_code}")

    except Exception as e:
        print("An error occurred:", e)

