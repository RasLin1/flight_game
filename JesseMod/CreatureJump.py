import random


from RasmusMod.game_functions import select_closest_airports,current_distance
from geopy.distance import geodesic
from RasmusMod.db import select_random_airport_location
def defMoveMonster(amount,coords) :
   movementDecision = random.randint(1,3)
   #deciding value for wether the monster stays or moves
   points= select_closest_airports(amount,coords)
   #selects an amount of close airports based on funtion defined amounts
   randomCloseAirport = random.randint(0,points.len()-1)
  #random value to pick a random airport from the close airports
   randomFarAirport = select_random_airport_location()
   #returns a random airport
   randomFarAirportDistance =current_distance(coords,(randomFarAirport["lat"],randomFarAirport["lon"]))
   #returns the distance of said aiport
   if movementDecision == 3 :
    jumpdistance = random.randint(1,15)
    #monster has decided to move
    if jumpdistance == 15:
        print("Creature move big now :(")

       # trough a while loop we make sure the airport is within bounds of a long distance jump
        #  and get a new point until it is withing set bounds so that we may return it
        while 2000>randomFarAirportDistance or randomFarAirportDistance>5000 :
            randomFarAirport = select_random_airport_location()
            randomFarAirportDistance = current_distance(coords, (randomFarAirport["lat"], randomFarAirport["lon"]))
        return randomFarAirport
    else:
        print("Creature move small now:)")

             #select a random airport in the list
        return points[randomCloseAirport]

   else:
        print("Creature stays :D")


