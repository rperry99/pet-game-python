import random


# Other Variables
game_running = True

# Starting Stats
health = 5
stamina = 5
max_stamina = 5
hunger = 0
weight = 3
strength = 1
happiness = 0
poo = False

# stages
rookie = False
champ = False
ultimate = False
mega = False

# Poo Function
def do_you_poo():
    poo_chance = [1, 2, 3, 4, 5, 6]
    does_poo = random.choice(poo_chance)
    if does_poo == 1 or does_poo == 3:
        global poo
        poo = True
        print("\nEw a pooie!")
    return


def level_up():
    stat_chance = [0, 1, 2, 3, 4, 5]
    global health
    global max_stamina
    global weight
    global strength
    health_up = random.choice(stat_chance)
    stamina_up = random.choice(stat_chance)
    weight_up = random.choice(stat_chance)
    strength_up = random.choice(stat_chance)
    print("Health + " + str(health_up))
    print("Stamina + " + str(stamina_up))
    print("Weight + " + str(weight_up))
    print("Strength + " + str(strength_up) + "\n")
    health += health_up
    max_stamina += stamina_up
    weight += weight_up
    strength += strength_up
    return


print("Hello, meet your digimon partner, Viximon!")
print("Let's give Viximon a name!")
digi_name = input("Enter Viximon's nickname: ")
print("Aww, " + digi_name + " is a great name!")

# Play the game
while game_running:
    print("What do you want to do with " + digi_name + "?")
    choice = input("1: Feed\n2: Train\n3: Play\n4: Clean\n5: Sleep\nS: Stats\nQ: Quit\nWhat do you want to do? ")

    # If Statements on choice
    if choice == "1":
        if hunger > 0:
            weight += 2
            hunger -= 1
            happiness += 1
            do_you_poo()
            print("\nNummy!\n")
        else:
            print("\n" + digi_name + " isn't hungry!\n")
    elif choice == "2":
        if stamina > 0:
            health += 2
            strength += 2
            stamina -= 1
            max_stamina += 1
            hunger += 1
            weight -= 1
            print("\nGettin' S W O L E!\n")
        else:
            print("\n" + digi_name + " is too tired, let them rest!\n")
    elif choice == "3":
        if stamina > 0:
            happiness += 2
            stamina -= 1
            print("\nHaving some fun!\n")
        else:
            print("\n" + digi_name + " is too tired, let them rest!\n")
    elif choice == "4":
        if poo:
            print("\nAll Clean!\n")
            poo = False
        else:
            print("\n" + digi_name + "'s cage is already clean!\n")
    elif choice == "5":
        stamina = max_stamina
        print("\nCatchin' some ZZZZs\n")
    elif choice == "s" or choice == "S":
        print("\nHealth: " + str(health))
        print("Stamina: " + str(stamina))
        print("Max Stamina: " + str(max_stamina))
        print("Hunger: " + str(hunger))
        print("Weight: " + str(weight))
        print("Strength: " + str(strength))
        print("Happiness: " + str(happiness) + "\n")
    elif choice == "q" or choice == "Q":
        game_running = False

    if strength >= 15 and 8 <= weight <= 12 and happiness >= 20 and rookie == False:
        print("\nWoah! " + digi_name + " transformed into a Renamon!\n")
        rookie = True
        level_up()
    if strength >= 30 and 20 <= weight <= 22 and happiness >= 40 and champ == False:
        print("\nCongratulations! " + digi_name + " transformed into a Kyubimon!\n")
        champ = True
        level_up()
    if strength >= 60 and 30 <= weight <= 35 and happiness >= 75 and not poo and ultimate == False:
        print("\nHoly Cow! " + digi_name + " transformed into a Taomon!\n")
        ultimate = True
        level_up()
    if strength >= 100 and weight == 50 and happiness >= 100 and not poo and mega == False:
        print("\nYou are the best handler! " + digi_name + " transformed into the highest level Sakuyamon!\n")
        mega = True
        level_up()








