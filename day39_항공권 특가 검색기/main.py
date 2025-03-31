# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.# noqa
import data_manager
import flight_search


datamanager = data_manager.DataManager()
sheet_data = datamanager.get_destination_data()

for city in sheet_data:
    flightsearch = flight_search.FlightSearch()
    if city['iataCode'] == "":
        city['iataCode'] = flightsearch.get_iatacode(city['city'])
    ticket_info = flightsearch.get_ticket(city['iataCode'])

print(ticket_info)
datamanager.destination_data = sheet_data
datamanager.iata_update()
