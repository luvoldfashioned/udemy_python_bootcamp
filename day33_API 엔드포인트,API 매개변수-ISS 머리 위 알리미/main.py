import requests
from datetime import datetime
import smtplib

EMAIL = "isthetestemail99@gmail.com"
PASSWORD = "irfwuyrmjclnxiof"

MY_LAT = 37.71267739692703  # Your latitude
MY_LONG = 127.18732262580288  # Your longitude


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT <= (iss_latitude+5)) and (MY_LAT >= (iss_latitude-5)):
        if (MY_LONG <= (iss_longitude+5)) and (MY_LAT >= (iss_latitude-5)):
            return True
        else:
            return False
    else:
        return False


def is_night(sunrise, sunset, now):
    if (now >= sunset) or (now <= sunrise):
        return True
    else:
        return False


# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()


UTC_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
UTC_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# 시차 계산
KST_sunrise = UTC_sunrise + 9
KST_sunset = UTC_sunset + 9

if KST_sunrise > 24:
    KST_sunrise -= 24
if KST_sunset < 0:
    KST_sunset += 24

time_now = datetime.now()

if is_night(KST_sunrise, KST_sunset, time_now.hour):
    if is_iss_close():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="storm6781@naver.com",
                msg="Subject:look up the sky\n\niss on your head!"
                )


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
