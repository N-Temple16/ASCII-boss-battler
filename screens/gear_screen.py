def gear_setup():
    print("Here Are You Options For Combat Styles:")
    print("[1] Magic")
    print("[2] Range")
    print("[3] Melee")
    choice = input("What will it be?: ")

    if choice == "1":
        print("You chose Magic")
    elif choice == "2":
        print("You chose Range")
    elif choice == "3":
        print("You chose Melee")
    else:
        print("Not an option")