from creatures import update_entity_health
from db import select_specific_creature, select_specific_player

def combat(player_id, creature_id):
    active_combat = True
    

    while active_combat:
        player = select_specific_player(player_id)
        enemy = select_specific_creature(creature_id)
        print(f"Pelaajan arvot ovat HP:{player["current_health"]} | DMG:{player["damage"]}")
        print(f"Vastustajan arvot ovat HP:{enemy["health"]} | DMG:{enemy["damage"]}")
        if player["current_health"] > 0 and enemy["health"]>0:
            player_action = input("Kirjoita 'H' niin hyökkäät | 'S' niin yrität siepata hirviön").upper()
            if player_action == "H":
                attack_success = update_entity_health(creature_id, -player["damage"], 2)
                if attack_success == True:
                    print(f"{player["player_name"]} teki {player["damage"]} DMG {enemy["name"]} vastaan")
            if player_action == "S":
                attack_success = update_entity_health(creature_id, -{player["damage"]}, 2)
                if attack_success == True:
                    print(f"{player["player_name"]} teki {player["damage"]} DMG {enemy["name"]} vastaan")

    