import requests
from func.Speak import speak


def get_top_headlines(api_key, country='in'):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Failed to retrieve news: {response.status_code}")
        return []


def Samachaarmain():
    api_key = '4bb53e03b278443691c59560db6767bf'
    print("Fetching top headlines of news in India...")
    speak("Fetching top headlines of news in India and to know more click on the URL provided below.")
    articles = get_top_headlines(api_key)
    if articles:
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published At: {article['publishedAt']}")
            print(f"   URL: {article['url']}")
            print("-" * 40)
    else:
        print("No news articles found.")



