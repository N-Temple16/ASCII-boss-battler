from utilities.text_colours import TextColours
from screens.battle_screen import initiate_battle_screen
from game_state import GameState

t = TextColours

def gear_setup(game_state):
    while True:
        print(f"{t.magenta}Here Are You Options For Combat Styles:{t.end}")
        print(f"{t.blue}[1] Magic{t.end}")
        print(f"{t.green}[2] Range{t.end}")
        print(f"{t.red}[3] Melee{t.end}")
        choice = input("What will it be?: ")

        style_choice = {
            "1": "magic",
            "2": "range",
            "3": "melee"
        }

        if choice in style_choice:
            selected_style = style_choice[choice]
            correct_choice = input(f"{t.magenta}Are you sure you want to choose {selected_style.title()}? [Y/N]:{t.end} ")
            if correct_choice.lower() == "y":
                game_state.combat_style = selected_style.lower()
                #game_state.apply_combat_style_modifiers()
                return initiate_battle_screen(game_state)
            elif correct_choice.lower() == "n":
                print("wise choice..")
            else:
                print("Invalid input. Please provide the correct input.")
        else:
            print("Invalid input. Input must be a number.")
