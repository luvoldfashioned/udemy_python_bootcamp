import requests
# from pprint import pprint

sheety_endpoint = "https://api.sheety.co/b1d8cf9b0fc5264c6be7eae6cae1d2eb/flightDeals/prices" # noqa


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.get_destination_data()

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def iata_update(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                    }
            }
            self.response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
                )
