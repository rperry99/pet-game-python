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

# Poo Function
def do_you_poo():
    "Random number for pooping"
    poo_chance = [1, 2, 3, 4, 5, 6]
    does_poo = random.choice(poo_chance)
    if does_poo == 1 or does_poo == 3 or does_poo == 5:
        poo = True
        print("\nEw a pooie!")
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
            weight += 1
            hunger -= 1
            happiness += 1
            do_you_poo()
            print("\nNummy!\n")
        else:
            print("\n" + digi_name + " isn't hungry!\n")
    elif choice == "2":
        if stamina > 0:
            health += 2
            strength += 1
            stamina -= 1
            max_stamina += 1
            hunger += 1
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






