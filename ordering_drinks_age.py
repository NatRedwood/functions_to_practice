import random

def drinks_age():
    alcoholic = ["whiskey", "coctail", "rum", "wine", "beer"]
    non_alcoholic = ["apple juice", "lemonade", "water", "soda", "coffee"]
    random_vs_chosen=(1,2)
    age = int(input("How old are you? \n"))
    if age > 5:
        random_vs_chosen=int(input("\nDo you want to get a random drink(1) or do you want to choose from the offer(2)? \nWrite the correct number: \n"))
        if  random_vs_chosen == 1 and age > 21:
            alc_nonalc = int(input("\nAlcoholic(1) or non-alcoholic(2)? \nWrite the correct number: \n"))
            if alc_nonalc == 1:
                print("\nDrink for you:\n", random.choice(alcoholic))
            if alc_nonalc == 2:
                print("\nDrink for you:\n", random.choice(non_alcoholic))
        if  random_vs_chosen == 2 and age > 21:
            alc_nonalc = int(input("\nAlcoholic(1) or non-alcoholic(2)? \nWrite the correct number: \n"))
            if alc_nonalc == 1:
                print("\nChoose from the offer:\n")
                for x in alcoholic:
                    print(x)
            if alc_nonalc == 2:
                print("\nChoose from the offer:\n")
                for x in non_alcoholic:
                    print(x)
        elif  random_vs_chosen == 1 and 21 > age > 15:
            print("\nDrink for you:\n", random.choice(non_alcoholic))
        elif  random_vs_chosen == 2 and 21 > age > 15:
            print("\nChoose from the offer:\n")
            for x in non_alcoholic:
                print(x)
        elif random_vs_chosen == 1 and age < 15:
            print("\nDrink for you:\n", random.choice(non_alcoholic[0:3]))
        elif random_vs_chosen == 2 and age < 15:
            print("\nChoose from the offer:\n")
            for x in non_alcoholic[0:3]:
                print(x)
    else:
        print("\nDrink for you:\n", non_alcoholic[0])
        
drinks_age()
