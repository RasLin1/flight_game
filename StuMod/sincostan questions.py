import random
acceptable = (0.2, 0.25, 0.4, 0.5, 0.6, 0.75, 0.8, 1)

def random_tan():
    side_a = random.randint(1, 101)
    side_b = random.randint(1, 101)
    while side_a/side_b not in acceptable:
        side_a = random.randint(1, 101)
        side_b = random.randint(1, 101)
    answer_tan_alpha = float(input(f"Mikä on kulman alpha tan, jos kulman viereinen sivu on {side_b} ja kulman vastapäätä oleva sivu on {side_a}: "))
    while answer_tan_alpha != side_a/side_b:
        answer_tan_alpha = float(input("Väärin, yritä uudestaan: "))
    print("Oikein! Hyvin ratkaistu.")
    return

def random_sin():
    side_a = random.randint(1, 101)
    side_c = random.randint(1, 101)
    while side_a / side_c not in acceptable:
        side_a = random.randint(1, 101)
        side_c = random.randint(1, 101)
    answer_sin_alpha = float(input(f"Mikä on kulman alpha sini, jos hypotenuusa on {side_c} ja kulman vastapäätä oleva sivu on {side_a}: "))
    while answer_sin_alpha != side_a / side_c:
        answer_sin_alpha = float(input("Väärin, yritä uudestaan: "))
    print("Oikein! Hyvin ratkaistu.")
    return

def random_cos():
    side_b = random.randint(1, 101)
    side_c = random.randint(1, 101)
    while side_b / side_c not in acceptable:
        side_b = random.randint(1, 101)
        side_c = random.randint(1, 101)
    answer_cos_alpha = float(input(f"Mikä on kulman alpha cosini, jos hypotenuusa on {side_c} ja kulman viereinen sivu on {side_b}: "))
    while answer_cos_alpha != side_b / side_c:
        answer_cos_alpha = float(input("Väärin, yritä uudestaan: "))
    print("Oikein! Hyvin ratkaistu.")
    return

command = input("Lopeta painamalla enter, valitse arvottava tehtävän anto (Tan, Cos, Sin): ")
while command != "":
    if command == "Tan" or command == "tan":
        random_tan()
        command = input("Lopeta painamalla enter, valitse arvottava tehtävän anto (Tan, Cos, Sin): ")
    elif command == "Cos" or command == "cos":
        random_cos()
        command = input("Lopeta painamalla enter, valitse arvottava tehtävän anto (Tan, Cos, Sin): ")
    elif command == "Sin" or command == "sin":
        random_sin()
        command = input("Lopeta painamalla enter, valitse arvottava tehtävän anto (Tan, Cos, Sin): ")
    else:
        command = input("Virheellinen komento.\nLopeta painamalla enter, valitse arvottava tehtävän anto (Tan, Cos, Sin): ")

print("Kiitos käytöstä.")