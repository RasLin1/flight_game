from creatures import update_entity_health
from db import select_specific_creature, select_specific_player

def combat(player_id, creature_id):
    player = select_specific_player(player_id)
    enemy = select_specific_creature(creature_id)
    active_combat = True

    while active_combat:
        print("This is combat")
        print(f"Player stats are: ")
        active_combat = False
    