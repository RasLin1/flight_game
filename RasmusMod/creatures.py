#Luo pelaajan sanakirjana
def create_entity(name, airport):

    return {
        "name": name,
        "country": airport["c_name"],
        "location": airport["ident"],
        "location_name":airport["a_name"],
        "cordinates": (airport["lat"], airport["lon"])
    }

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
    
