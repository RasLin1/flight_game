import mysql.connector
import random

important_player_id = 0

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
    airport_amount_query = "SELECT COUNT(*) FROM airport WHERE airport.type = 'large_airport' AND airport.continent =  'EU'"
    cursor = db.cursor()
    cursor.execute(airport_amount_query)
    query_return = cursor.fetchone()
    airport_count = query_return[0]
    airport_number = random.randint(0, (airport_count - 1))
    airport_rand_query = f"SELECT airport.name AS a_name, airport.ident AS ident, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS c_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.type = 'large_airport' AND airport.continent =  'EU' LIMIT 1 OFFSET %s "
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_rand_query, (airport_number,))
        query_return = cursor.fetchone()
        if query_return:
            cursor.close()
            return query_return
        else:
            print("DEBUG: Error returning specific airport")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return []
    

#Ottaa lentokenttä  icao koodin  inputtina  ja hakee sen  kentokentän tietokannasta. 
def select_specific_airport(icao):
    db = db_connection()
    airport_query = "SELECT airport.name AS a_name, airport.ident AS ident, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS c_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.type = 'large_airport' AND airport.continent =  'EU' AND ident = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query, (icao,))
        query_return = cursor.fetchone()
        if query_return:
           cursor.close()
           return query_return
        else:
            print("DEBUG: Error returning specific airport")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return []
        

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
    cursor.close()

# Hakee kaikki lentokentät tietystä maasta
def select_airports_by_country(country_code):
    db = db_connection()
    airport_query = f"SELECT airport.name AS airport_name, airport.ident AS airport_icao, airport.type AS airport_type, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS country_name FROM airport INNER JOIN country  ON airport.iso_country = country.iso_country WHERE airport.iso_country = %s AND airport.type NOT IN ('heliport', 'seaplane_base', 'closed')"
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query)
        query_return = cursor.fetchall()
        if query_return:
            cursor.close()
            return query_return
        else:
            print(f"Ei löytynyt lentokenttiä maalle: {country_code}")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return []

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
            cursor.close()
            return query_return
        else:
            print("Tapahtumaa ei löytynyt")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return []


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
    cursor.close()
    db.close()

def move_player(player, new_location):
    db = db_connection()
    create_player_query = f"UPDATE player SET player_location = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_player_query, (new_location, player["id"]))
        db.commit()
        if cursor.rowcount > 0:
            print(f"DEBUG: Player {player['name']} moved to {new_location}")
            cursor.close()
            return True
        else:
            print("DEBUG: No player updated — check player ID or location.")
            cursor.close()
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return False
    
#Tästä alkaa hirviö jutskat
def create_game_monster(name, location):
    db = db_connection()
    select_creature = select_random_creature()
    create_game_creature_query = f"INSERT INTO game_creatures (player_id, creature_id, creature_location, creature_current_health) VALUES (%s, %s, %s, %s)"
    try: 
        print(f"DEBUG: player_id={important_player_id}, creature_id={select_creature['creature_id']}, location={location}")
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_game_creature_query, (important_player_id, select_creature["creature_id"], location, select_creature["creature_max_health"]))
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
    cursor.close()
    db.close()

def select_random_creature():
    db = db_connection()
    monster_amount_query = "SELECT COUNT(*) FROM creature"
    cursor = db.cursor()
    cursor.execute(monster_amount_query)
    query_return = cursor.fetchone()
    creature_count = query_return[0]
    creature_number = random.randint(0, (creature_count - 1))
    random_creature_query = f"SELECT * FROM creature LIMIT 1 OFFSET %s "
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(random_creature_query, (creature_number,))
        query_return = cursor.fetchone()
        print("DEBUG random creature:", query_return)
        if query_return:
            cursor.close()
            return query_return
        else:
            print("Hirviöö ei löytynyt")
            cursor.close()
            return []
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return []

def move_creature(creature, new_location):
    db = db_connection()
    create_player_query = f"UPDATE player SET player_location = %s WHERE player_id = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(create_player_query, (new_location, player["id"]))
        db.commit()
        if cursor.rowcount > 0:
            print(f"DEBUG: Player {player['name']} moved to {new_location}")
            cursor.close()
            return True
        else:
            print("DEBUG: No player updated — check player ID or location.")
            cursor.close()
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        cursor.close()
        return False