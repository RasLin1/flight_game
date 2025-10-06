import mysql.connector

yhteys = mysql.connector.connect (
    host = "127.0.0.1",
    port = 3306,
    database="monster_game",
    user = "monster_game",
    password = "teamseven",
    autocommit = True




)


def deleteCreatureData (Id) :
    sql = f"DELETE FROM creature WHERE creature_id = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (Id,))
# delete creature from database. Currently command gets denied
def insertCreatureTable(Id,Name,Health,Damage):
   #sql =f"UPDATE creature SET creature_name = %s ,creature_damage=%s,creature_max_health=%s WHERE creature_id = %s "
   sql = f"INSERT into creature (creature_id,creature_name,creature_max_health,creature_damage) VALUES (%s,%s,%s,%s)"
   kursori = yhteys.cursor(dictionary=True)
   kursori.execute(sql,(Id,Name,Health,Damage))
# Add desired creature to the database with required parameters

   return
def updateCreature(Id,Health) :
    sql = f"UPDATE creature SET creature_max_health = creature_max_health-%s WHERE creature_id =%s"
    kursori= yhteys.cursor(dictionary=True)
    kursori.execute(sql, (Health,Id))
    # update current health of creature for combat purposes

    return
def selectCreature(Id):
    sql = "SELECT * FROM creature WHERE creature_id = %s"
    try:
        kursori = yhteys.cursor(dictionary=True)
        kursori.execute(sql, (Id,))
        query_return = kursori.fetchone()
        print("selectCreature", query_return)
        return query_return
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    kursori.close()
    #for debugging to see if data exists
def insertItem(Id,Name,Damage,Desc):
    sql = f"INSERT into items (item_id,item_type,item_damage,item_description) VALUES (%s,%s,%s,%s) "
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql,(Id,Name,Damage,Desc))
# add new item to database with  required parameters
def selectItem(Id):
    sql = "SELECT * FROM items WHERE item_id = %s"
    try:
        kursori = yhteys.cursor(dictionary=True)
        kursori.execute(sql, (Id,))
        query_return = kursori.fetchone()
        print("selectItem",query_return)
        return query_return
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")

#insertAlienTable(3,"Scytheworm",100,10 )
selectCreature(3)
#insertItem(1,"Axe",50,"Strong weapon that can cut trough rough exoskeleton")
selectItem(1)
#deleteAlienData(3)