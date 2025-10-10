from creatures import update_entity_health
from db import select_specific_creature, select_specific_player

def combat(player_id, creature_id):
    player = select_specific_player(player_id)
    enemy = select_specific_creature(creature_id)
    active_combat = True
    

    while active_combat:
        print(f"Player stats are HP:{player["current_health"]}. Damage:{player["damage"]}")
        print(f"Enemy stats are HP:{enemy["health"]}. Damage:{enemy["damage"]}")
        if player["current_health"] > 0 and enemy["health"]>0:
            player_action = input("Kirjoita 'H' niin hyökkäät | 'S' niin yrität siepata hirviön")
            if player_action == "H":
                attack_success = update_entity_health(creature_id, -{player["damage"]}, 2)
                if attack_success == True:
                    print(f"")

    