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
        from_='+19123485062',
        to='+8201083181785'
    )
print(message.status)