# Name: Trevor McDonough
# Final project: Scripting Languages
# Date: 4/23/23

import random

# Create a dictionary for player attributes
player = {
    "name": "",
    "class": "",
    "health": 10,
    "attack": 1,
    "defense": 0,
    "gold": 0
}

# Create a dictionary for enemy attributes
enemy = {
    "name": "",
    "health": 0,
    "attack": 0,
    "defense": 0,
    "gold": 0
}

# Define a function to generate a random enemy
def generate_enemy():
    enemy_types = ["Goblin", "Orc", "Troll", "Dragon"]
    enemy_type = random.choice(enemy_types)
    if enemy_type == "Goblin":
        return {
            "name": "Goblin",
            "health": 5,
            "attack": 2,
            "defense": 1,
            "gold": random.randint(1, 5)
        }
    elif enemy_type == "Orc":
        return {
            "name": "Orc",
            "health": 10,
            "attack": 4,
            "defense": 2,
            "gold": random.randint(5, 10)
        }
    elif enemy_type == "Troll":
        return {
            "name": "Troll",
            "health": 15,
            "attack": 6,
            "defense": 3,
            "gold": random.randint(10, 15)
        }
    else:
        return {
            "name": "Dragon",
            "health": 20,
            "attack": 8,
            "defense": 4,
            "gold": random.randint(15, 20)
        }

# Define a function to start the game
def start_game():
    print("Welcome to the DnD Simulator!")
    player["name"] = input("What is your name? ")
    player["class"] = input("What class would you like to play? ")
    print("Welcome, " + player["name"] + ", the " + player["class"] + "!")
    print("Your starting stats are:")
    print("Health: " + str(player["health"]))
    print("Attack: " + str(player["attack"]))
    print("Defense: " + str(player["defense"]))
    print("Gold: " + str(player["gold"]))
    while True:
        choice = input("Would you like to continue? (Y/N) ")
        if choice.upper() == "Y":
            play_round()
        else:
            print("Thanks for playing!")
            break

# Define a function to play a round of the game
def play_round():
    enemy = generate_enemy()
    print("A wild " + enemy["name"] + " appears!")
    while enemy["health"] > 0:
        action = input("What would you like to do? (Attack/Run) ")
        if action.lower() == "attack":
            attack_damage = player["attack"] + random.randint(1, 5) - enemy["defense"]
            if attack_damage <= 0:
                attack_damage = 1
            print("You deal " + str(attack_damage) + " damage to the " + enemy["name"] + "!")
            enemy["health"] -= attack_damage
            if enemy["health"] <= 0:
                print("You defeated the " + enemy["name"] + "!")
                player["gold"] += enemy["gold"]
                print("You found " + str(enemy["gold"]) + " gold!")
                print("Your total gold is now " + str(player["gold"]) + ".")
        elif action.lower() == "run":
                print("You ran away you coward!")
                print("Thanks for playing!")
                break
        else:
                print("Thanks for playing!")
                break