from db import select_specific_airport, select_airports_per_country,  select_all_airports
import creatures
from geopy.distance import geodesic

def current_distance(l1, l2):
        final_distance = geodesic(l1, l2).km
        return "%.2f" % final_distance
    
def look_up_airports(country_iso):
    airports = select_airports_per_country(country_iso)
    return airports

def select_closest_airports(amount, player_cordinates):
    airports = select_all_airports()
    airport_distances  = []
    for x in airports:
         distance = current_distance(player_cordinates, (x["lat"], x["lon"]))
         distance_float = float(distance)
         if distance_float == 0.0:
              continue
         temp_airport_dictionary = {"airport_name": x["airport_name"],"airport_icao": x["airport_icao"], "distance": distance}
         airport_distances.append(temp_airport_dictionary)
    airport_distances.sort(key=lambda a: float(a["distance"]))
    closest_airports = airport_distances[:amount]
    return closest_airports

def move(entity, icao):
    updated_airport = creatures.move_entity(entity, select_specific_airport(icao))
    return updated_airport

def get_cordinates(airport):
    return  (airport["lat"], airport["lon"])