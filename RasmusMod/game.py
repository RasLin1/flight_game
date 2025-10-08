from db import select_random_airport_location, select_random_event
import creatures
import game_functions

allow_game = True

def play():
    round = 1
    player = creatures.create_entity("Pelaaja", select_random_airport_location(), 1)
    monster = creatures.create_entity("Hirviö", select_random_airport_location(), 2)

    while allow_game:
        distance = game_functions.current_distance(player['cordinates'], monster['cordinates'])
        print(f"{player['name']} located in {player['location_name']} {player['location']} distance to {monster['name']} {distance}km") 
        if distance == 0.00:
            print("Same airport as monster")
        else:
            airports = game_functions.select_closest_airports(5, player['cordinates'])
            for x in airports:
                print(f"Nimi: {x["airport_name"]} | ICAO-koodi: {x["airport_icao"]} | Distance: {x["distance"]}")
            round_action = input("Kirjoita 'S' jos haluat siirtää paikkaa | Kirjoita 'L' jos haluat levätä ").upper()
            if round_action == "S":
                updated_player = game_functions.move(player, input("Anna lentokentän icao-koodi jonne haluat siirtyä: ").upper())
                player = updated_player
            elif round_action == "L":
                print("ZZZ...")
            else:
                print("Move invalid input")
        round = round + 1
        print(round)

if __name__ == '__main__':
    play()