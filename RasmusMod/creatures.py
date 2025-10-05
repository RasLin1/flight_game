from game_functions import get_cordinates

#Luo pelaajan sanakirjana
def create_entity(name, airport):
    return {
        "name": name,
        "country": airport["c_name"],
        "location": airport["ident"],
        "location_name":airport["a_name"],
        "cordinates": get_cordinates(airport)
    }

def move_entity(entity, airport):
    entity["location"] = airport["ident"]
    entity["cordinates"] = (airport["lat"], airport["lon"])
    return {
        "name": entity["name"],
        "country": airport["c_name"],
        "location": airport["ident"],
        "location_name":airport["a_name"],
        "cordinates": get_cordinates(airport)
    }
    
