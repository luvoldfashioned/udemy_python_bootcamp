import datetime as dt
import smtplib
import random

EMAIL = "isthetestemail99@gmail.com"
PASSWORD = "irfwuyrmjclnxiof"

file = open(file="quotes.txt", mode="r")
data = file.read()
quote_list = data.split("\n")


now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open(file="quotes.txt", mode="r") as file:
        # data = file.read()
        # quote_list = data.split("\n")
        quote_list = file.readlines()
        quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="storm6781@naver.com",
            msg=f"Subject:motivational quote\n\n{quote}"
            )
