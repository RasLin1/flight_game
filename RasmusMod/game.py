from db import select_random_airport_location, select_random_event, select_specific_airport
import creatures
import game_functions

allow_game = True

def play():
    round = 1
    #Luo pelaajan sekä hirviön tietokanassa ja säästää tärkeät tiedot muuntaijiin
    player = creatures.create_entity("Pelaaja", select_random_airport_location(), 1)
    monster = creatures.create_entity("Hirviö", select_random_airport_location(), 2)

    while allow_game:
        #Pelaaja vuoro alkaa tästä
        #Kertoo etäisyyden pelaajan ja hirviön välillä
        distance = float(game_functions.current_distance(player['cordinates'], monster['cordinates']))
        #Jos pelaaja ja hirviö ovat samalla lentokentältä niin palaajan pitäisi taistella hirviön kanssa
        if distance == 0.00:
            print("Located in same airport as monster")
        #Kertoo missä pelaaja on
        print(f"{player['name']} located in {player['location_name']} {player['location']} distance to {monster['name']} {distance}km") 
        #Hakee ensimmäisen arvon määrä lentokenttiä
        airports = game_functions.select_closest_airports(5, player['cordinates'])
        #Tulostaa kaikki lähimmät lentokentät
        for x in airports:
            print(f"Nimi: {x["airport_name"]} | ICAO-koodi: {x["airport_icao"]} | Distance: {x["distance"]}")
        round_action = input("Kirjoita 'S' jos haluat siirtää paikkaa | Kirjoita 'L' jos haluat levätä ").upper()
        if round_action == "S":
            #Päivittää pelajan sijainin
            player = creatures.move_entity(player, select_specific_airport(input("Anna lentokentän icao-koodi jonne haluat siirtyä: ").upper()), 1)
        elif round_action == "L":
            print("ZZZ...")
        else:
            print("Move invalid input")
        round = round + 1
        print(round)

if __name__ == '__main__':
    play()