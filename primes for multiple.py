def Prime():
    # welcome
    print("Hello! This software checks if some numbers are prime.")
    # x
    while True:
        try:
            End = int(input("Please type where to count to:"))
        except:
            print("Invalid number, try new number.")
            End = int(input("Please type where to count to:"))
        else:
            break
    while End < 0:
        print("Invalid number, try new number.")
        End = int(input("Please type number:"))
    list_of_numbers = [1, 2, 3]
    current = 3
    while current < End:
        current += 1
        # optimization
        y = current // 2
        # loop
        while y >= 1:
            if y == 1:
                list_of_numbers.append(current)
                break
            elif current % y == 0:
                break
            else:
                y -= 1
        continue
    print(list_of_numbers)

    # ask for next
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