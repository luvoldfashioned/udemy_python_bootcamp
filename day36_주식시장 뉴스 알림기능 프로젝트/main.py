import requests
from twilio.rest import Client
from random import choice

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = ""
auth_token = ""

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ""
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News"). # noqa
stock_response = requests.get(STOCK_ENDPOINT, params=stock_param)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

closing_price = [value["4. close"] for (key, value) in stock_data.items()]
yesterday = float(closing_price[0])
day_before = float(closing_price[1])

difference = yesterday - day_before
if difference < 0:
    difference = -difference
    up_or_down = "?–¼"
else:
    up_or_down = "?–²"

percentage = round((difference / day_before) * 100, 2)


# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. # noqa
NEWS_PARAM = {
    "q": COMPANY_NAME,
    "apiKey": "",
}

if percentage > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAM)
    news_data = news_response.json()

    articles = news_data["articles"][:3]

    article_separate = [{"title": value['title'],
                        "description": value['description']} for value in articles]

    chosen_article = choice(article_separate)
    completion_message = f"{STOCK_NAME}: {up_or_down}{percentage}\nHeadline: {chosen_article['title']}\nBrief: {chosen_article['description']}"

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=completion_message,
            from_='+',
            to='+'
        )
    print(message.status)
