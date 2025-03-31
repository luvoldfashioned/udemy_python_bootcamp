# This class is responsible for talking to the Flight Search API.
import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
API_KEY = "GGwX9ns7C1gX8Pk6uJBwG4Brw6EwdneU"


class FlightSearch:
    def get_iatacode(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY}
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            url=location_endpoint,
            params=query,
            headers=headers
        )
        data = response.json()["locations"]
        iata_code = data[0]["code"]
        return iata_code

    def get_ticket(self, city_code):

        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

        date_from = tomorrow.strftime('%d/%m/%Y')
        date_to = six_month_from_today.strftime('%d/%m/%Y')

        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        response = requests.get(
            url=search_endpoint,
            params=query,
            headers=headers
        )
        data = response.json()
        return data
