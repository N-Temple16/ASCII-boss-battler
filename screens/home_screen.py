from screens.gear_screen import gear_setup
from utilities.text_colours import TextColours

t = TextColours

def show_home_screen():
    while True:
        try:
            print(f"{t.magenta}Welcome To Boss Battle Sim{t.end}")
            print(f"{t.red}[1] Fight{t.end}")
            print(f"{t.yellow}[2] Exit{t.end}")
            choice = input("Choose an option: ")

            if choice == "1":
                gear_setup()
            elif choice == "2":
                print("Exiting Game")
                break
            else:
                print("not a correct choice >:()")
        except ValueError:
            print("Invalid input. Please enter a number.")
        