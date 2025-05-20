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
                while True:
                    try:
                        if correct_choice == "Y" or correct_choice == "y":
                            initiate_battle_screen()
                            break
                        elif correct_choice == "N" or correct_choice == "n":
                            print("wise choice..")
                            break
                        #else:
                            #print("Invalid input. Please provide the correct input.")
                    except ValueError:
                        print("Invalid input. Please provide the correct input.")
                #break
            else:
                print("Invalid input. Input must be a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")