import random
import math

def random_hypotenuse():
    side_a = random.randint(1, 25)
    side_b = random.randint(1, 25)
    attempts = 0
    answer = int(input(
        f"Mikä on hypotenuusan karkea pituus, jos suorakulmaisen kolmion muut sivut ovat {side_a} ja {side_b}?\n"
        f"Anna vastaus kokonaislukuna, pyöristettynä poikkeuksellisesti alaspäin: "))
    while attempts <= 3 and answer != (math.sqrt(side_a**2 + side_b**2)) // 1:
        answer = int(input("Väärin, yritä uudestaan: "))
        attempts += 1
    if attempts > 3 and answer != (math.sqrt(side_a**2 + side_b**2)) // 1:
        print ("Valitettavasti en voi sinua nyt palkita. Parempi onni seuraavan kysymyksen kanssa.")
    else:
        sql = "SELECT event_reward_type, event_reward_value FROM events WHERE event_description = 'hypotens';"
        # print(sql)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(f"Oikein! Palkinnoksi saat {result['event_reward_value']} {result['event_reward_type']}")
        # tähän vielä lisää updaten pelaajan resursseihin
    return

#command = input("Lopeta painamalle enter, jatka antamalla mikä tahansa stringgi: ")
#while command != "":
    random_hypotenuse()
    command = input("Lopeta painamalle enter, jatka antamalla mikä tahansa stringgi: ")

#print("Kiitos käytöstä.")