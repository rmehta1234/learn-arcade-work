import random


def main():
    done = False
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    drinks_in_canteen = 3

    print()

    # intro
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and outrun the natives.")

    # questions
    while not done:
        print()
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        # answering each question
        native_distance_increment = random.randrange(7, 14)
        choice = input("Your choice? ").lower()
        if choice == "q":
            done = True
            print()
            print("Game Over.")
        elif choice == "e":
            print()
            print("Miles travelled:", miles_travelled, "/ 200")
            print("Camel tiredness:", camel_tiredness, "/ 8")
            print("Thirst level:", thirst, "/ 6")
            print("Drinks in canteen:", drinks_in_canteen, "/ 3")
            print("The natives are", miles_travelled - natives_distance, "miles behind you")

        elif choice == "d":
            camel_tiredness = 0
            print("Your camel is happy.")
            natives_distance = native_distance_increment + natives_distance
        elif choice == "c":
            travel_increment = random.randrange(10, 20)
            miles_travelled += travel_increment
            print("You travelled", travel_increment, "miles.")
            if random.randrange(20) == 0:
                print("You have found an oasis!")
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = 3
            else:
                thirst += 1
                camel_tiredness += random.randrange(1, 3)
                natives_distance = native_distance_increment + natives_distance
        elif choice == "b":
            travel_increment = random.randrange(5, 12)
            miles_travelled += travel_increment
            print("You travelled", travel_increment, "miles.")
            if random.randrange(20) == 0:
                print("You have found an oasis!")
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = 3
            else:
                thirst += 1
                camel_tiredness += 1
                natives_distance = native_distance_increment + natives_distance
        elif choice == "a":
            if drinks_in_canteen > 0:
                thirst = 0
                drinks_in_canteen -= 1
            else:
                print("You do not have any more drinks.")

        # warnings
        if not done:
            if thirst >= 6:
                print("You died of thirst! Game Over.")
                done = True
            elif thirst >= 4:
                print("You are thirsty")

        if not done:
            if camel_tiredness >= 8:
                print("Your camel is dead. Game Over.")
                done = True
            elif camel_tiredness >= 5:
                print("Your camel is getting tired.")

        if not done:
            if natives_distance > miles_travelled:
                print("The natives caught up to you. Game Over.")
                done = True
            elif natives_distance > miles_travelled - 15:
                print("The natives are getting close!")

        if not done and miles_travelled >= 200:
            print("You have won the game!")
            done = True


main()
