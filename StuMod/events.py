import random
from hypotens import random_hypotenuse
from sincostan_questions import random_tan, random_cos, random_sin

def random_event():
    event_selection = random.randint(1, 5)
    if event_selection == 1:
        random_hypotenuse()
    elif event_selection == 2:
        random_sin()
    elif event_selection == 3:
        random_cos()
    elif event_selection == 4:
        random_tan()
    else:
        riddle = random.randint(1, 12)
        sql = "SELECT * FROM events WHERE event_id = riddle;"
        # print(sql)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchall()
        answer = input(result["event_description"])
        attempts = 0
        while attempts <= 3 and answer != result['answer']:
            answer = int(input("Väärin, yritä uudestaan: "))
            attempts += 1
        if attempts > 3 and answer != result['answer']:
            print("Valitettavasti en voi sinua nyt palkita. Parempi onni seuraavan kysymyksen kanssa.")
        else:
            print(f"Oikein! Palkinnoksi saat {result['event_reward_value']} {result['event_reward_type']}")
            # tähän vielä lisää updaten pelaajan resursseihin