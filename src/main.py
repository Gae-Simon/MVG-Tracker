from datetime import datetime
from datetime import timedelta
import json

import mvg_api

if __name__ == '__main__':
    u_bahn_station_id = mvg_api.get_id_for_station("Olympia-Einkaufszentrum")
    bus_station_id = mvg_api.get_id_for_station("Dessauerstraße")

    u_bahn_lines = mvg_api.get_lines(u_bahn_station_id)
    bus_station_lines = mvg_api.get_lines(bus_station_id)

    u_bahn_departures = mvg_api.get_departures(u_bahn_station_id, 5)
    bus_departures = mvg_api.get_departures(bus_station_id, 5)

    print("------------------------")
    print("OLYMPIA-EINKAUFSZENTRUM")
    for i in range(10):
        print(u_bahn_departures[i]["product"] + " -- " + u_bahn_departures[i]["label"] + " -- " + str(
            mvg_api._convert_time(u_bahn_departures[i]["departureTime"])))
    print("------------------------")
    print("DESSAUERSTRASSE")
    for i in range(10):
        print(bus_departures[i]["product"] + " -- " + bus_departures[i]["label"] + " -- " + str(
            mvg_api._convert_time(bus_departures[i]["departureTime"])))
    print("------------------------")
