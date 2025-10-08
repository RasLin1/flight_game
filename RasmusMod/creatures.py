from game_functions import get_cordinates
from db import create_player


#Luo pelaajan sanakirjana
def create_entity(name, airport, type):
    print(f"DEBUG: create_player() called with name={name}, location={airport["ident"]}")
    entity = {
        "name": name,
        "country": airport["c_name"],
        "location": airport["ident"],
        "location_name":airport["a_name"],
        "cordinates": (airport["lat"], airport["lon"])
    }
    if type == 1:
        player = create_player(name, airport["ident"])
        if player == True:
            print("Player creation success")
        else:
            print("Player creation fail")
    return entity

def move_entity(entity, airport):
    if airport == False:
        print("Error in moving, possibly invalid icao")
        return {
            "name": entity["name"],
            "country": entity["country"],
            "location": entity["location"],
            "location_name":entity["location_name"],
            "cordinates": entity["cordinates"]
        }
    else:
        return {
            "name": entity["name"],
            "country": airport["c_name"],
            "location": airport["ident"],
            "location_name":airport["a_name"],
            "cordinates": (airport["lat"], airport["lon"])
        }
    
