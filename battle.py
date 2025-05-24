#battle options would just be like the menus
import random
from utilities.text_colours import TextColours
from boss import Boss
from utilities.ascii_art import defeated_mole

t = TextColours

def player_battle_options(game_state):
    boss = game_state.boss

    def activate_prayer(game_state, style: str):
        if game_state.prayer >= 15:
            game_state.ispraying = True
            game_state.praying_against = style
            print(f"You begin protecting yourself from {style.capitalize()} attacks")
        else:
            game_state.prayer = 0
            print("You do not have any prayer remaining to protect yourself")
            return False
        return True

    while boss.health > 0 and game_state.health > 0:
        print(f"{t.magenta}The {boss.name} is about to attack with {boss.combat_style[0].title()}{t.end}")
        print(f"{t.magenta}Choose what you want to do:{t.end}")
        print(f"{t.cyan}[1] Attack{t.end}")
        print(f"{t.cyan}[2] Protect from Magic{t.end}")
        print(f"{t.cyan}[3] Protect from Range{t.end}")
        print(f"{t.cyan}[4] Protect from Melee{t.end}")
        print(f"{t.cyan}[5] Stop Protecting{t.end}")
        print(f"{t.cyan}[6] Eat Food{t.end}")
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
                if not activate_prayer(game_state, "magic"):
                    continue
            case "3":
                if not activate_prayer(game_state, "range"):
                    continue
            case "4":
                if not activate_prayer(game_state, "melee"):
                    continue
            case "5":
                game_state.ispraying = False
                game_state.praying_against = ""
                print("You stop praying")
                continue
            case "6":
                if game_state.health == 100:
                    print("You are already full health, why would you want to do that?")
                    continue
                elif game_state.food == 0:
                    print(f"{t.red}You have no food left{t.end}")
                    continue
                else:
                    game_state.food -= 1
                    game_state.health = min(game_state.health + 8, 100)
                    print(f"{t.green}Your health goes up to {game_state.health}{t.end}")
                    print(f"{t.green}You have {game_state.food} food left{t.end}")
            case _:
                print("invalid input")
                continue
        
        if boss.health > 0:
            if game_state.ispraying and game_state.prayer >= 15:
                game_state.prayer -= 15
                game_state.prayer = max(game_state.prayer, 0)

                if game_state.prayer <= 30 and game_state.prayer > 0:
                    print(f"{t.yellow}⚠️  Your prayer is getting low: {game_state.prayer} remaining!{t.end}")

                if game_state.praying_against == boss.combat_style[0]:
                    print("You are praying against the bosses attack and therefore take no damage")
                    print(f"Your prayer drains by 15 leaving you with {game_state.prayer}")
                else:
                    print("You are not praying against the correct combat style and the boss attempts to still hit you")
                    print(f"Your prayer drains by 15 leaving you with {game_state.prayer}")
                    
                    if random.randint(1, 100) <= boss.accuracy:
                        boss_damage_dealt = random.randint(boss.damage_range[0], boss.damage_range[1])
                        game_state.health -= boss_damage_dealt
                        print(f"{t.red}The boss strikes back and deals {boss_damage_dealt} damage!{t.end}")
                        print(f"{t.red}Your health goes down to {game_state.health}{t.end}")
                    else:
                        print(f"{t.red}You caught a break, the {boss.name} missed!{t.end}")
            else:
                if game_state.ispraying:
                    print("You're trying to pray, but you've run out of prayer points!")
                    game_state.ispraying = False
                    game_state.praying_against = None

                if random.randint(1, 100) <= boss.accuracy:
                    boss_damage_dealt = random.randint(*boss.damage_range)
                    game_state.health -= boss_damage_dealt
                    print(f"{t.red}The boss hits you for {boss_damage_dealt} damage!{t.end}")
                    print(f"{t.red}Your health drops to {game_state.health}{t.end}")
                else:
                    print(f"{t.red}The boss misses! You take no damage.{t.end}")
        elif boss.health <= 0:
            print(f"Well done, you have slain the {boss.name}!")
            print(defeated_mole)
            break
        
        if game_state.health <=0:
            print("Oh dear, you have died!")
            break
        