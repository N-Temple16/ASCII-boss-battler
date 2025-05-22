#battle options would just be like the menus
import random
from utilities.text_colours import TextColours
from boss import Boss
from utilities.ascii_art import defeated_mole

t = TextColours

def player_battle_options(game_state):
    boss = game_state.boss

    print("Choose what you want to do:")
    print(f"{t.red}[1] Attack{t.end}")
    print(f"{t.cyan}[2] Protect from Magic{t.end}")
    print(f"{t.cyan}[3] Protect from Range{t.end}")
    print(f"{t.cyan}[4] Protect from Melee{t.end}")
    print(f"{t.yellow}[5] Eat Food{t.end}")
    #for testing the hit chance
    while True:
        choice = input("What will it be?: ")

        match choice:
            case "1":
                if random.randint(1, 100) <= game_state.accuracy:
                    print(f"{t.green}successful hit!{t.end}")
                    damage_dealt = random.randint(game_state.damage_range[0], game_state.damage_range[1])
                    boss.health -= damage_dealt
                    if boss.health <= 0:
                        boss.health = 0
                        print(f"Well done, you have slain the {boss.name}!")
                        print(defeated_mole)
                        break
                    print(f"{t.green}you hit a {damage_dealt}{t.end}")
                    print(f"{t.green}the boss's health is now {boss.health}{t.end}")
                else:
                    print(f"{t.red}oh no you missed!{t.end}")
            case "2":
                print("this does nothing for now")
            case "3":
                print("this also does nothing for now")
            case "4":
                print("this was the correct prayer... but still does nothing for now")
            case "5":
                if game_state.health < 100:
                    game_state.food -= 1
                    game_state.health += 8
                    if game_state.health > 100:
                        game_state.health = 100
                    print(f"{t.green}Your health goes up to {game_state.health}{t.end}")
                else:
                    print("you are already full health, why would you want to do that?")
            case "6":
                print("you found the hidden option")
                game_state.health -= 10
                print(f"{t.red}Your health goes down to {game_state.health}{t.end}")

def boss_battle_options():
    pass

"""
Then it would be the bosses turn after each player input. The bosses won't pray or eat so their only option each turn is to attack the player
"""