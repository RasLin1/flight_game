import mysql.connector

yhteys = mysql.connector.connect (
    host = "127.0.0.1",
    port = 3306,
    database="monster_game",
    user = "monster_game",
    password = "teamseven",
    autocommit = True




)
def olioLisays(alienId,alienName) :
    healthValue = float(input("Anna alieenin health arvo :"))
    damageValue = float(input("Anna alieenin damage arvo :"))

    return  alienId,alienName,healthValue,damageValue
#newAlien = olioLisays(1,"Scytheworm")



def updateAlienTable(Id,Name,Health,Damage):
   #sql =f"UPDATE creature SET creature_name = %s ,creature_damage=%s,creature_max_health=%s WHERE creature_id = %s "
   sql = f"INSERT into creature (creature_id,creature_name,creature_max_health,creature_damage) VALUES (%s,%s,%s,%s)"
   kursori = yhteys.cursor(dictionary=True)
   kursori.execute(sql,(Id,Name,Health,Damage))


   return
def selectAlien(Id):
    sql = "SELECT * FROM creature WHERE creature_id = %s"
    try:
        kursori = yhteys.cursor(dictionary=True)
        kursori.execute(sql, (Id,))
        query_return = kursori.fetchone()
        print(query_return)
        return query_return
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    kursori.close()

#updateAlienTable(3,"Scytheworm",100,10 )
selectAlien(3)