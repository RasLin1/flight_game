from db import create_player, move_player, create_game_creature, move_creature


#Luo pelaajan sanakirjana
def create_entity(name, airport, type):
    print(f"DEBUG: create_player() called with name={name}, location={airport["ident"]}")
    if type == 1:
        player = create_player(name, airport["ident"])
        if player == False:
            print("Player creation fail")
            return False
        else:  
            print("Player creation success")
            entity = {
                "name": name,
                "id": player,
                "country": airport["c_name"],
                "location": airport["ident"],
                "location_name":airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"])
            }
            return entity
    if type == 2:
        creature = create_game_creature(name, airport["ident"])
        if creature == False:
            print("Monster creation fail")
            return False
        else:  
            print("Player creation success")
            entity = {
                "name": name,
                "id": creature,
                "country": airport["c_name"],
                "location": airport["ident"],
                "location_name":airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"])
            }
            return entity
    return entity

def move_entity(entity, airport, type):
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
        if type == 1:
            player = move_player(entity, airport["ident"])
            if player == True:
                print("Creature creation success")
                return {
                "name": entity["name"],
                "country": airport["c_name"],
                "location": airport["ident"],
                "location_name":airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"])
                }
            else:
                print("Creature creation fail")
                return entity
            
        elif type == 2:
            creature = move_creature(entity, airport["ident"])
            if player == True:
                print("Creature creation success")
            else:
                print("Creature creation fail")
                return entity
            return {
                "name": entity["name"],
                "country": airport["c_name"],
                "location": airport["ident"],
                "location_name":airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"])
            }
    
