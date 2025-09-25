from game_functions import get_cordinates

#Luo pelaajan sanakirjana
def create_entity(name, airport):
    return {
        "name": name,
        "location": airport["ident"],
        "coordinates": get_cordinates(airport)
    }

def move_entity(entity, airport):
    entity["location"] = airport["ident"]
    entity["coordinates"] = (airport["latitude_deg"], airport["longitude_deg"])
    return {
        "name": entity["name"],
        "location": airport["ident"],
        "coordinates": get_cordinates(airport)
    }
    

