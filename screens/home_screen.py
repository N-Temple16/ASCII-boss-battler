from screens.gear_screen import gear_setup
from utilities.text_colours import TextColours

t = TextColours

def show_home_screen(game_state):
    while True:
        print(f"{t.magenta}Welcome To Boss Battle Sim{t.end}")
        print(f"{t.red}[1] Fight{t.end}")
        print(f"{t.yellow}[2] Exit{t.end}")
        choice = input("Choose an option: ")

        if choice == "1":
            return gear_setup(game_state)
        elif choice == "2":
            print("Exiting Game")
            return False
        else:
            print("not a correct choice >:()")
        