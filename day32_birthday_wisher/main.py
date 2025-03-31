import pandas as pd
import datetime as dt
import smtplib
import random

letter_templates = ["letter_templates/letter_1.txt",
                    "letter_templates/letter_2.txt",
                    "letter_templates/letter_3.txt"]

MY_EMAIL = "isthetestemail99@gmail.com"
MY_PASSWORD = "irfwuyrmjclnxiof"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")

birthday_dict = {
    (data_row.month, data_row.day): (data_row["name"], data_row["email"], data_row["year"], data_row["month"], data_row["day"]) for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_email = birthday_dict[today][1]
    birthday_name = birthday_dict[today][0]
    chosen_template = random.choice(letter_templates)

    with open(chosen_template, "r") as template_file:
        template = template_file.read()
        letter = template.replace("[NAME]", birthday_name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
