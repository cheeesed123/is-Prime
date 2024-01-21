def Prime():
    # welcome
    print("Hello! This software checks if a number is prime.")
    # x
    while True:
        try:
            x = int(input("Please type number:"))
        except:
            print("Invalid number, try new number.")
            x = int(input("Please type number:"))
        else:
            break
    while x < 0:
        print("Invalid number, try new number.")
        x = int(input("Please type number:"))
    # optimization
    y = x // 2
    # loop
    while y > 1:
        if x % y == 0:
            print("Not Prime")
            break
        else:
            y -= 1
            continue
    if y == 1:
        print("Prime")

    print("Want to check another number?")
    while True:
        try:
            x = str(input("(y/n):")).lower().strip()
        except:
            print("Invalid choice, try new choice.")
            x = str(input("(y/n)")).lower().strip()
        else:
            break
    
    while True:
        if x == "y":
            Prime()
        elif x == "n":
            print("Bye!")
            break
        else:
            print("Invalid choice, try new choice.")
            x = str(input("(y/n)")).lower().strip()
            continue
    exit
Prime()