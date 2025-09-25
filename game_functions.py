from db import select_specific_airport, select_airports_per_country
import creatures
from geopy.distance import geodesic

def current_distance(l1, l2):
        final_distance = geodesic(l1, l2).km
        return "%.2f" % final_distance
    
def look_up_airports(country_iso):
    airports = select_airports_per_country(country_iso)
    return airports


def move(entity, icao):
    updated_airport = creatures.move_entity(entity, select_specific_airport(icao))
    if updated_airport == False:
        print("Error in moving plane, possibly invalid icao")
        return False
    else:
        print(f"New ICAO-code: {updated_airport['location']}")
        return updated_airport

def get_cordinates(airport):
    return  (airport["latitude_deg"], airport["longitude_deg"])