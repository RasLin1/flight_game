import random


from RasmusMod.game_functions import select_closest_airports,current_distance
from geopy.distance import geodesic
from RasmusMod.db import select_random_airport_location
def defMoveMonster(amount,coords) :
   movementDecision = random.randint(1,3)
   points= select_closest_airports(amount,coords)
   randomCloseAirport = random.randint(0,points.len()-1)
   randomFarAirport = select_random_airport_location()
   randomFarAirportDistance =current_distance(coords,(randomFarAirport["lat"],randomFarAirport["lon"]))
   if movementDecision == 3 :
    jumpdistance = random.randint(1,15)
    if jumpdistance == 15:
        print("Creature move big now :(")

        while 2000>randomFarAirportDistance or randomFarAirportDistance>5000 :
            randomFarAirport = select_random_airport_location()
            randomFarAirportDistance = current_distance(coords, (randomFarAirport["lat"], randomFarAirport["lon"]))
        return randomFarAirport
    else:
        print("Creature move small now:)")


        return points[randomCloseAirport]

   else:
        print("Creature stays :D")


