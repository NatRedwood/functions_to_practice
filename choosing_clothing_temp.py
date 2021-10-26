def clothing():
    summer_clothes = ["sunglasses", "swimsuit", "sunscreen", "shorts"]
    clothes = [summer_clothes, "short sleeves", "coat", "jacket"]
    seasons = ["spring","summer","autumn","winter"]
    temp = int(input("What's the temperature today?\n"))
    leaves = ["yes", "no"]
    if temp < 10:
        print("\nOh, it's cold. It's probably",seasons[3]+"!","\nYou should wear a", clothes[3])
    elif 10 < temp < 20:
        print("\nIt's hard to say. It's ", seasons[0], " or ", seasons[2]+".")
        leaves = str(input("\nDo the leaves fall down? (yes/no)\n"))
        if leaves == "yes":
            print("\nIt's ", seasons[2]+"!","\nPut your ", clothes[2], "on.")
        else:
            print("\nIt's ", seasons[0]+"!", "\nYou'll need ", clothes[1]+".")
    else:
        print("\nYaaay, it's ", seasons[1],"!!!\n", "\nChoose one of those:\n")
        for x in summer_clothes:
            print (x)
    print("\n\n\nPS.: Remember, I do Celsius, not Fahrenheit.")
            

clothing()
