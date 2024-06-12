import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = 'https://ekantipur.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h1', class_='')
        articles = soup.find_all('p', id=4)
        news = 'Headline:\n'
        for headline in headlines:
            news += headline.get_text(strip=True) + '\n'
        news += 'Article\n'
        for article in articles:
            news += article.get_text(strip=True) + '\n'
        return news
    else:
        return "Failed to fetch news"