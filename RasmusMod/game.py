from db import select_random_airport_location, select_random_event, select_specific_airport, update_player_value, select_specific_player
import creatures
import game_functions
from combat import combat
import random

allow_game = True

def play():
    round = 1
    probes = []
    #Luo pelaajan sekä hirviön tietokanassa ja säästää tärkeät tiedot muuntaijiin
    player = creatures.create_entity(input("Anna pelaajan nimi: "), select_random_airport_location(), 1)
    monsters = []
    for x in range(3):
        entity = creatures.create_entity(f"Ent{x}", select_random_airport_location(), 2)
        if entity:
            monsters.append(entity)
        else:
            print(f"DEBUG: Skipping failed monster creation for Ent{x}")

    while allow_game:
        #Pelaaja vuoro alkaa tästä
        #Kertoo  pelaajan sijainin
        print(f"{player['name']} sijainti {player['location_name']} on {player['location']}")
        #Kertoo etäisyyden pelaajan ja hirviön välillä
        for monster in monsters:
            distance = float(game_functions.current_distance(player['cordinates'], monster['cordinates']))
            #Jos pelaaja ja hirviö ovat samalla lentokentältä niin palaajan pitäisi taistella hirviön kanssa
            if distance == 0.00:
                print(f"{player['name']} on samalla lentokentällä kuin {monster['name']}")
                player_action = input(f"Kirjoita 'T' jos haluat taistella | Kirjoita 'P' jos haluat yrittää paeta: ").upper()
                creature_action = random.randint(1, 3)
                if player_action == "P":
                    if creature_action == 3:
                        print("Yrität paeta mutta hirviö hyökkää")
                        combat(player["id"], monster["id"])
                    else:
                        closest_airport = game_functions.select_closest_airports(1, player["cordinates"])
                        player = creatures.move_entity(player, closest_airport["airport_icao"], 1)

            #Kertoo missä pelaaja on
            print(f"{player['name']} etäisyys {monster['name']} {distance}km") 
        #Hakee ensimmäisen arvon määrä lentokenttiä
        airports = game_functions.select_closest_airports(8, player['cordinates'])
        #Tulostaa kaikki lähimmät lentokentät
        for x in airports:
            print(f"Nimi: {x["airport_name"]} | ICAO-koodi: {x["airport_icao"]} | Distance: {x["distance"]}")
        round_action = input("Kirjoita 'S' jos haluat siirtää paikkaa | Kirjoita 'L' jos haluat levätä: ").upper()
        if round_action == "S":
            #Päivittää pelajan sijainin
            player = creatures.move_entity(player, select_specific_airport(input("Anna lentokentän icao-koodi jonne haluat siirtyä: ").upper()), 1)
        elif round_action == "L":
            event = select_random_event()
            print(event["event_description"])
            user_answer = input("Kirjoita vastaus saadaksesi palkinnon: ")
            if user_answer == event["event_answer"]:
                print("Right answer")
                reward_return = update_player_value(event["event_reward_type"], event["event_reward_value"], player["id"])
                if reward_return:
                    print(select_specific_player(player["id"]))
            else:
                print("Wrong answer")
            print("ZZZ...")
        else:
            print("Move invalid input")
        #The monsters turn begins here
        temp_monster_holder = []
        for monster in monsters:
            new_monster_location = creatures.move_entity(monster, select_specific_airport(monster["location"]), 2)
            temp_monster_holder.append(new_monster_location)
        monsters = temp_monster_holder
        round = round + 1
        print(round)

if __name__ == '__main__':
    play()