import random
import math

def random_hypotenuse():
    side_a = random.randint(1, 25)
    side_b = random.randint(1, 25)
    answer = int(input(
        f"Mikä on hypotenuusan karkea pituus, jos suorakulmaisen kolmion muut sivut ovat {side_a} ja {side_b}?\n"
        f"Anna vastaus kokonaislukuna, pyöristettynä poikkeuksellisesti alaspäin: "))
    while answer != (math.sqrt(side_a**2 + side_b**2)) // 1:
        answer = int(input("Väärin, yritä uudestaan: "))
    print("Oikein!")
    return

command = input("Lopeta painamalle enter, jatka antamalla mikä tahansa stringgi: ")
while command != "":
    random_hypotenuse()
    command = input("Lopeta painamalle enter, jatka antamalla mikä tahansa stringgi: ")

print("Kiitos käytöstä.")