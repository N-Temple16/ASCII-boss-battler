from screens.gear_screen import gear_setup

def show_home_screen():
    print("Welcome To Boss Battle Sim")
    print("[1] Fight")
    print("[2] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        gear_setup()
    elif choice == "2":
        print("Exiting Game")
    else:
        print("not a correct choice >:()")
        