from db import create_player, move_player, create_game_creature, move_creature, select_random_airport_location, update_player_health, update_creature_health
from game_functions import select_closest_airports, current_distance
import random

#Luo pelaajan sanakirjana
def create_entity(name, airport, type):
    print(f"DEBUG: create_player() called with name={name}, location={airport["airport_icao"]}")
    if type == 1:
        player = create_player(name, airport["airport_icao"])
        if player == False:
            print("Player creation fail")
            return False
        else:  
            print("Player creation success")
            entity = {
                "name": name,
                "id": player,
                "country": airport["c_name"],
                "location": airport["airport_icao"],
                "location_name": airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"]),
                "fuel": 100,
            }
            return entity
    elif type == 2:
        creature = create_game_creature(name, airport["airport_icao"])
        if creature == False:
            print("Monster creation fail")
            return False
        else:  
            print("Monster creation success")
            entity = {
                "name": name,
                "id": creature,
                "country": airport["c_name"],
                "location": airport["airport_icao"],
                "location_name": airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"])
            }
            return entity
    else:
        print("DEBUG: Invalid entity type")

def move_entity(entity, airport, type):
    if airport == False:
        print("Error in moving, possibly invalid icao")
        return {
            "name": entity["name"],
            "id": entity["id"],
            "country": entity["country"],
            "location": entity["location"],
            "location_name": entity["location_name"],
            "cordinates": entity["cordinates"],
            "fuel": entity["fuel"]
        }
    else:
        if type == 1:
            current_fuel = entity["fuel"] - (float(current_distance(entity["cordinates"], (airport["lat"], airport["lon"])))/100)
            player = move_player(entity, airport["airport_icao"], current_fuel)
            print(f"Polttoaine liikeen jälkeen on {current_fuel}")
            if player == True:
                print("Player movement success")
                return {
                "name": entity["name"],
                "id": entity["id"],
                "country": airport["c_name"],
                "location": airport["airport_icao"],
                "location_name": airport["a_name"],
                "cordinates": (airport["lat"], airport["lon"]),
                "fuel": current_fuel
                }
            else:
                print("Creature movement fail")
                return entity
            
        elif type == 2:
            print(f"DEBUG: Creature named {entity["name"]} starting movement")
            creature_movement_decision = creature_movement(entity["cordinates"])
            print(f"DEBUG: Movement returned: {creature_movement_decision}")
            if creature_movement_decision == False:
                print(f"DEBUG: Creature named {entity["name"]} doesn't want to move")
                return entity
            else:
                creature = move_creature(entity, creature_movement_decision["airport_icao"])
                if creature == True:
                    print(f"DEBUG: Creature named {entity["name"]} moved succesfully")
                else:
                    print(f"DEBUG: Creature named {entity["name"]} didn't move succesfully")
                    return entity
                return {
                    "name": entity["name"],
                    "id": entity["id"],
                    "country": airport["c_name"],
                    "location": airport["airport_icao"],
                    "location_name": airport["a_name"],
                    "cordinates": (airport["lat"], airport["lon"])
                }

#Updates the health of an entity
def update_entity_health(id, health_change, type):
    if type == 1:
        player = update_player_health(id, health_change)
        if player == True:
            print("DEBUG: Player health change success")
            return True
        else:
            print("DEBUG: Player health change fail")
            return  False
    elif type == 2:
        creature = update_creature_health(id, health_change)
        if creature == True:
            print(f"DEBUG: Creature health changed succesfully")
            return True
        else:
            print(f"DEBUG: Creature health didn't change succesfully")
            return False

#The movement  logic for creatures
def creature_movement(cordinates):
   movement_decision = random.randint(1,3)
   #deciding value for wether the monster stays or moves
   points = select_closest_airports(10 ,cordinates)
   #selects an amount of close airports based on funtion defined amounts
   random_close_airport = random.randint(0, 9)
  #random value to pick a random airport from the close airports
   random_far_airport = select_random_airport_location()
   #returns a random airport
   random_far_airport_distance = float(current_distance(cordinates,(random_far_airport["lat"],random_far_airport["lon"])))
   #returns the distance of said aiport
   if movement_decision == 3 :
    jump_distance = random.randint(1,15)
    #monster has decided to move
    if jump_distance == 15:
        print("DEBUG: Creature move big now :(")
       # trough a while loop we make sure the airport is within bounds of a long distance jump
        #  and get a new point until it is withing set bounds so that we may return it
        while 500.00>random_far_airport_distance or random_far_airport_distance>2000.00 :
            random_far_airport = select_random_airport_location()
            random_far_airport_distance = float(current_distance(cordinates, (random_far_airport["lat"], random_far_airport["lon"])))
        return random_far_airport
    else:
        print("DEBUG: Creature move small now :)")
        #select a random airport in the list
        return points[random_close_airport]

   else:
        print("DEBUG: Creature stays :D")
        return False