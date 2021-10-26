def vote_age():
    name = str(input("1) What's your name? \n"))
    age = int(input("\n2) How old are you? \n"))
    if age > 18:
        print("\nEligibility decision: ", name, "is eligible to vote.")
    elif 15 < age < 18:
        print("\nYou can vote but you need to do more paperwork.")
    else:
        print("\nEligibility decision: ", name, "is not eligible to vote.")

vote_age()
