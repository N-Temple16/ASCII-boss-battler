from utilities.text_colours import TextColours
from screens.battle_screen import initiate_battle_screen
from battle import pause_and_clear
from game_state import GameState
import json

t = TextColours

def gear_setup(game_state):
    with open("data/combat_styles.json") as file:
            combat_styles = json.load(file)

    style_choice = {
        "1": "magic",
        "2": "range",
        "3": "melee"
    }

    while True:
        print(f"{t.magenta}Here Are Your Options For Combat Styles:{t.end}")
        print(f"{t.blue}[1] Magic{t.end}")
        print(f"{t.green}[2] Range{t.end}")
        print(f"{t.red}[3] Melee{t.end}")
        choice = input("What will it be?: ")

        if choice in style_choice:
            selected_style = style_choice[choice]
            selected_stats = combat_styles[selected_style]

            print(f"""{t.cyan}
Your stats for the {selected_style.title()} combat style are as follows: 
Health = {selected_stats["health"]}, 
Prayer = {selected_stats["prayer"]}, 
Food = {selected_stats["food"]}, 
Accuracy = {selected_stats["accuracy"]}, 
Damage range = {selected_stats["damage_range"]}{t.end}
""")
            correct_choice = input(f"{t.magenta}Are you sure you want to choose {selected_style.title()}? [Y/N]:{t.end} ")
            if correct_choice.lower() == "y":
                game_state.combat_style = selected_style.lower()
                return initiate_battle_screen(game_state)
            elif correct_choice.lower() == "n":
                print("Wise choice..")
                pause_and_clear()
            else:
                print("Invalid input. Please provide the correct input.")
                pause_and_clear()
        else:
            print("Invalid input. Input must be a number.")
