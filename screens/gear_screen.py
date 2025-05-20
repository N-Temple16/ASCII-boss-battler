from utilities.text_colours import TextColours
from screens.battle_screen import initiate_battle_screen

t = TextColours

def gear_setup():
    while True:
        try:
            print(f"{t.magenta}Here Are You Options For Combat Styles:{t.end}")
            print(f"{t.blue}[1] Magic{t.end}")
            print(f"{t.green}[2] Range{t.end}")
            print(f"{t.red}[3] Melee{t.end}")
            choice = input("What will it be?: ")

            if choice == "1" or choice == "2" or choice == "3":
                correct_choice = input(f"{t.magenta}Are you sure you want to choose that type? [Y/N]:{t.end} ")
                if correct_choice.lower() == "y":
                    initiate_battle_screen()
                    break
                elif correct_choice.lower() == "n":
                    print("wise choice..")
                else:
                    print("Invalid input. Please provide the correct input.")
            else:
                print("Invalid input. Input must be a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")