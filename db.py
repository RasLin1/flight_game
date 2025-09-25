import mysql.connector
import random

#Tietokantaan liityvät funktiot alkavat tästä
#Tietokanta connector
def db_connection():
        return mysql.connector.connect(
            host="127.0.0.1",
            port = 3306,
            database = "",
            user="",
            password=""
        )

#Arpoo random lentokentän  ja  palautta sen
def select_random_airport_location():
    db = db_connection()
    airport_amount_query = "SELECT COUNT(*) FROM airport WHERE airport.type = 'large_airport' AND airport.continent =  'EU'"
    cursor = db.cursor()
    cursor.execute(airport_amount_query)
    query_return = cursor.fetchone()
    airport_count = query_return[0]
    airport_number = random.randint(0, (airport_count - 1))
    airport_rand_query = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport WHERE airport.type = 'large_airport' AND airport.continent =  'EU' LIMIT 1 OFFSET %s "
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_rand_query, (airport_number,))
        query_return = cursor.fetchone()
        if query_return:
            return query_return
        else:
            print("Lentokenttä ei löytynyt")
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    cursor.close()

#Ottaa lentokenttä  icao koodin  inputtina  ja hakee sen  kentokentän tietokannasta. 
def select_specific_airport(icao):
    db = db_connection()
    airport_query = "SELECT name, ident, latitude_deg, longitude_deg FROM airport WHERE airport.type = 'large_airport' AND airport.continent =  'EU' AND ident = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query, (icao,))
        query_return = cursor.fetchone()
        if query_return:
           return query_return
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    cursor.close()

#Ottaa maan koodin ja sen perusteella  hakee sekä palauttaa tiedot
def select_airports_per_country(country_code):
    db = db_connection()
    airport_query = f"SELECT airport.name AS airport_name, airport.ident AS airport_icao, airport.type AS airport_type, airport.latitude_deg AS lat, airport.longitude_deg AS lon, country.name AS country_name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE airport.iso_country = %s AND airport.type = 'large_airport' AND airport.continent =  'EU'"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(airport_query, (country_code,))
        query_return = cursor.fetchall()
        if query_return:
            return query_return
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    cursor.close()