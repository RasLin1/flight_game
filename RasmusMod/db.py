import mysql.connector
import random

#Tässsä tiedostossa löytyy tietokantaan liityviä kyselyitä
#Tietokanta connector
def db_connection():
        return mysql.connector.connect(
            host="127.0.0.1",
            port = 3306,
            database = "monster_game",
            user="monster_game",
            password="teamseven"
        )

#"airport" tauluun liityvät kyselyt alkavat tästä
#Arpoo satunnaisen lentokentän  ja  palautta sen
def select_random_airport_location():
    db = db_connection()
    airport_rand_query = f"SELECT airport.name AS a_name, airport.ident AS airport_icao, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS c_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.type = 'large_airport' AND airport.continent =  'EU' ORDER BY RAND() LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_rand_query)
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("DEBUG: Error returning specific airport")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()
    

#Ottaa lentokenttä  icao koodin  inputtina  ja hakee sen  kentokentän tietokannasta. 
def select_specific_airport(icao):
    db = db_connection()
    airport_query = "SELECT airport.name AS a_name, airport.ident AS airport_icao, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS c_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.type = 'large_airport' AND airport.continent =  'EU' AND ident = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query, (icao,))
        query_return = cursor.fetchone()
        if query_return:
           return query_return
        else:
            print("DEBUG: Error returning specific airport")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()
        

#Hakee kaikki lentokentät  tietokannasta
def select_all_airports():
    db = db_connection()
    airport_query = f"SELECT airport.name AS airport_name, airport.ident AS airport_icao, airport.type AS airport_type, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS country_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.type = 'large_airport' AND airport.continent =  'EU'"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query)
        query_return = cursor.fetchall()
        if query_return:
            return query_return
        else:
            print("DEBUG: Error returning all airports list")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    finally:
        cursor.close()
        db.close()

# Hakee kaikki lentokentät tietystä maasta
def select_airports_by_country(country_code):
    db = db_connection()
    airport_query = f"SELECT airport.name AS airport_name, airport.ident AS airport_icao, airport.type AS airport_type, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS country_name FROM airport INNER JOIN country  ON airport.iso_country = country.iso_country WHERE airport.iso_country = %s AND airport.type NOT IN ('heliport', 'seaplane_base', 'closed')"
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query)
        query_return = cursor.fetchall()
        if query_return:
            return query_return
        else:
            print(f"Ei löytynyt lentokenttiä maalle: {country_code}")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()

#"event" tauluun liityvät kyselyt alkavat tästä
#Arpoo satunnaisen tapahtuman ja palautta sen
def select_random_event():
    db = db_connection()
    event_amount_query = "SELECT COUNT(*) FROM events"
    cursor = db.cursor()
    cursor.execute(event_amount_query)
    query_return = cursor.fetchone()
    event_count = query_return[0]
    event_number = random.randint(0, (event_count - 1))
    random_event_query = f"SELECT * FROM events LIMIT 1 OFFSET %s "
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(random_event_query, (event_number,))
        query_return = cursor.fetchone()
        print("DEBUG random event:", query_return)
        if query_return:
            return query_return
        else:
            print("Tapahtumaa ei löytynyt")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()


#Tästä alkaa pelaajaan liityvät kyselyt

def create_player(name, location):
    global important_player_id
    db = db_connection()
    create_player_query = f"INSERT INTO player (player_name, player_location, fuel, money, max_health, current_health, game_score, game_completed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_player_query, (name, location, 100, 100, 100, 100, 0, False))
        db.commit()
        important_player_id = cursor.lastrowid
        if important_player_id:
            return important_player_id
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    finally:
        cursor.close()
        db.close()

#Hakee pelaajan käyttäen id arvoa"
def select_specific_player(id):
    db = db_connection()
    specific_creature_query = f"SELECT * FROM player WHERE player_id = %s LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(specific_creature_query, (id, ))
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("Hirviöö ei löytynyt")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()

def move_player(player, new_location, current_fuel):
    db = db_connection()
    create_player_query = f"UPDATE player SET player_location = %s, fuel = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_player_query, (new_location, current_fuel, player["id"]))
        db.commit()
        if cursor.rowcount > 0:
            print(f"DEBUG: Player {player['name']} moved to {new_location}")
            return True
        else:
            print("DEBUG: No player updated — check player ID or location.")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()
    
def update_player_health(player, health_change):
    db = db_connection()
    select_player_query = f"SELECT current_health FROM player WHERE player_id = %s"
    cursor = db.cursor(dictionary=True)
    cursor.execute(select_player_query, (player["id"]))
    query_return = cursor.fetchone()
    new_health = query_return["current_health"] + (health_change)
    update_player_query = f"UPDATE player SET current_health = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_player_query, (new_health, player["id"]))
        db.commit()
        if cursor.rowcount > 0:
            print(f"Players health is now {new_health}")
            return True
        else:
            print("DEBUG: Error in updating player health")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()

#Modular funktion that works for player fuel or money
def update_player_value(value_name, value_change, id):
    allowed_columns  = ["fuel", "money"]
    if value_name not in allowed_columns:
        print(f"DEBUG: Invalid column name: {value_name}")
        return False
    db = db_connection()
    select_player_query = f"SELECT {value_name} FROM player WHERE player_id = %s"
    cursor = db.cursor(dictionary=True)
    cursor.execute(select_player_query, (id, ))
    query_return = cursor.fetchone()
    new_value = query_return[f"{value_name}"] + (value_change)
    cursor =  db.cursor()
    update_player_query = f"UPDATE player SET {value_name} = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_player_query, (new_value, id))
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("DEBUG: Error in updating value health")
            return False
    except mysql.connector.Error as err:
        print("DEBUG: Error while updating player value")
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()

#Tästä alkaa hirviö jutskat
#Luo valitse ja luo hirviön peliä varten
def create_game_creature(name, location):
    db = db_connection()
    select_creature = select_random_creature()
    create_game_creature_query = f"INSERT INTO game_creatures (player_id, creature_id, creature_location, creature_current_health, creature_captured) VALUES (%s, %s, %s, %s, %s)"
    try: 
        print(f"DEBUG: player_id={important_player_id}, creature_id={select_creature['creature_id']}, location={location}")
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_game_creature_query, (important_player_id, select_creature["creature_id"], location, select_creature["creature_max_health"], False))
        db.commit()
        print("DEBUG: Insert executed successfully!")
        creature_id = cursor.lastrowid
        print(f"DEBUG: lastrowid={creature_id}")
        if creature_id:
            return creature_id
        else:
            print("DEBUG: No ID returned — insert may have failed or triggered constraint.")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    finally:
        cursor.close()
        db.close()

#Hakee random hirviön
def select_random_creature():
    db = db_connection()
    random_creature_query = f"SELECT * FROM creature ORDER BY RAND() LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(random_creature_query)
        query_return = cursor.fetchone()
        print("DEBUG random creature:", query_return)
        if query_return:
            return query_return
        else:
            print("Hirviöö ei löytynyt")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()

#Hakee hirviön käyttäen id arvoa"
def select_specific_creature(id):
    db = db_connection()
    specific_creature_query = f"SELECT creature_id FROM game_creature WHERE id = %s LIMIT 1"
    cursor = db.cursor()
    cursor.execute(specific_creature_query(id))
    creature_id = cursor.fetchone()
    cursor.close()
    specific_creature_query = f"SELECT * FROM creature WHERE creature_id = %s LIMIT 1"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(specific_creature_query(creature_id))
        query_return = cursor.fetchone()
        print("DEBUG random creature:", query_return)
        if query_return:
            return query_return
        else:
            print("Hirviöö ei löytynyt")
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return []
    finally:
        cursor.close()
        db.close()

def move_creature(creature, new_location):
    db = db_connection()
    move_creature_query = f"UPDATE game_creatures SET creature_location = %s WHERE id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(move_creature_query, (new_location, creature["id"]))
        db.commit()
        if cursor.rowcount > 0:
            print(f"DEBUG: Creature {creature['name']} moved to {new_location}")
            return True
        else:
            print("DEBUG: No creature updated — check creature ID or location.")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return False
    finally:
        cursor.close()
        db.close()

def update_creature_health(creature, health_change):
    db = db_connection()
    select_player_query = f"SELECT current_health FROM game_creatures WHERE player_id = %s"
    cursor = db.cursor(dictionary=True)
    cursor.execute(select_player_query, (creature["id"]))
    query_return = cursor.fetchone()
    new_health = query_return["current_health"] + (health_change)
    update_player_query = f"UPDATE player SET current_health = %s WHERE id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(update_player_query, (new_health, creature["id"]))
        db.commit()
        if cursor.rowcount > 0:
            print(f"{creature["name"]} health is now {new_health}")
            return True
        else:
            print("DEBUG: Error in updating player health")
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return False
    finally:
        cursor.close()
        db.close()
