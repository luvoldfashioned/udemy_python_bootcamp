# import smtplib

# my_email = "isthetestemail99@gmail.com"
# password = "irfwuyrmjclnxiof"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="storm6781@naver.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#         )

import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)
print(type(year))
if year == 2023:
    print("Wear a face mask")

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)
