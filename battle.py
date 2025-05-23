#battle options would just be like the menus
import random
from utilities.text_colours import TextColours
from boss import Boss
from utilities.ascii_art import defeated_mole

t = TextColours

def player_battle_options(game_state):
    boss = game_state.boss

    print("Choose what you want to do:")
    while boss.health > 0 and game_state.health > 0:
        print(f"{t.cyan}[1] Attack{t.end}")
        print(f"{t.cyan}[2] Protect from Magic{t.end}")
        print(f"{t.cyan}[3] Protect from Range{t.end}")
        print(f"{t.cyan}[4] Protect from Melee{t.end}")
        print(f"{t.cyan}[5] Eat Food{t.end}")
        choice = input("What will it be?: ")

        match choice:
            case "1":
                if random.randint(1, 100) <= game_state.accuracy:
                    print(f"{t.green}successful hit!{t.end}")
                    damage_dealt = random.randint(game_state.damage_range[0], game_state.damage_range[1])
                    boss.health -= damage_dealt
                    if boss.health <= 0:
                        boss.health = 0
                    print(f"{t.green}you hit a {damage_dealt}{t.end}")
                    print(f"{t.green}the boss's health is now {boss.health}{t.end}")
                else:
                    print(f"{t.red}oh no you missed!{t.end}")
            case "2":
                game_state.ispraying = True
            case "3":
                game_state.ispraying = True
            case "4":
                game_state.ispraying = True
            case "5":
                if game_state.health == 100:
                    print("You are already full health, why would you want to do that?")
                elif game_state.food == 0:
                    print(f"{t.red}You have no food left{t.end}")
                else:
                    game_state.food -= 1
                    game_state.health = min(game_state.health + 8, 100)
                    print(f"{t.green}Your health goes up to {game_state.health}{t.end}")
                    print(f"{t.green}You have {game_state.food} food left{t.end}")
            case "6":
                print("you found the hidden option")
                game_state.health -= 10
                print(f"{t.red}Your health goes down to {game_state.health}{t.end}")
            case _:
                print("invalid input")
                continue
        
        if boss.health > 0:
            if random.randint(1, 100) <= boss.accuracy:
                boss_damage_dealt = random.randint(boss.damage_range[0], boss.damage_range[1])
                game_state.health -= boss_damage_dealt
                print(f"{t.red}The boss strikes back and deals {boss_damage_dealt} damage!{t.end}")
                print(f"{t.red}Your health goes down to {game_state.health}{t.end}")
            else:
                print(f"{t.red}You caught a break, the {boss.name} missed!{t.end}")
        elif boss.health <= 0:
            print(f"Well done, you have slain the {boss.name}!")
            print(defeated_mole)
            break
        
        if game_state.health <=0:
            print("Oh dear, you have died!")
            break


"""
Then it would be the bosses turn after each player input. The bosses won't pray or eat so their only option each turn is to attack the player
"""