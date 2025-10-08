from db import  select_all_airports
from geopy.distance import geodesic

#Ottaa l1 ja l2 monikot, palauttaa etäisyyden kilometreina
def current_distance(l1, l2):
        final_distance = geodesic(l1, l2).km
        return "%.2f" % final_distance

#Ottaa  sisään  toivotun määrän  palauttaita sekä verratavat koordinaatit. Palauttaa listan täynnä sanakirjoja lentokenttien nimen, icao-koodin ja  etäisyyksien kanssa
def select_closest_airports(amount, player_cordinates):
    airports = select_all_airports()
    airport_distances  = []
    for x in airports:
         distance = float(current_distance(player_cordinates, (x["lat"], x["lon"])))
         if distance == 0.0:
              continue
         temp_airport_dictionary = {"airport_name": x["airport_name"],"airport_icao": x["airport_icao"], "distance": distance}
         airport_distances.append(temp_airport_dictionary)
    airport_distances.sort(key=lambda a: float(a["distance"]))
    closest_airports = airport_distances[:amount]
    return closest_airports
