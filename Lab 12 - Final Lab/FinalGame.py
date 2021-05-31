import random


def main():
    done = False
    money = 1000
    print()

    # intro
    print("Welcome to The Casino Game!")
    print("You are in debt for $20,000. Debt collectors are expecting the money in 30 minutes, or you will be arrested.")
    print("With $500, you have 30 minutes to make $20,000 .")

    # questions
    while not done:
        print()
        print("Menu")
        print("A. Roulette.")
        print("B. Slots.")
        print("C. Check balance")
        print("Q. Quit.")
        # answering each question
        choice = input("Your choice? ").lower()
        if choice == "q":
            done = True
            print()
            print("Game Over.")
            print("Your balance is $", money)
        elif choice == "a":
            # call roulette function
            money = roulette(money)
        elif choice == "b":
            # call slots
            money = slots(money)
        elif choice == "c":
            print("Balance: $", money)


def roulette(money):
    print("roulette")
    return money


def slots(money):
    done = False
    while not done:
        print()
        print("Slots:")
        print("A. Spin")
        print("B. Check balance")
        print("C. Menu")
        choice = input("Your choice? ").lower()
        if choice == "c":
            done = True
            print()
        elif choice == "b":
            print("Balance: $", money)
        elif choice == "a":
            if money < 200:
                print()
                print("You have an insufficient balance.")
                done = True
            else:
                print()
                print("Spend more money to earn bigger prizes!")
                print("A. Spend 200 dollars")
                print("B. Spend 500 dollars")
                choice = input("Your choice? ").lower()
                if choice == "a":
                    money -= 200
                    slot_one = random.randrange(3)
                    slot_two = random.randrange(3)
                    slot_three = random.randrange(5)
                    if slot_one == slot_two and slot_one == slot_three:
                        if random.randrange(10) == 5:
                            print()
                            print("You won the $10,000 jackpot!")
                            money += 10000
                        else:
                            print()
                            print("You won $3,000!")
                            money += 3000
                    else:
                        if slot_one == slot_two or slot_one == slot_three or slot_two == slot_three:
                            if random.randrange(7) == 0:
                                print()
                                print("You won $1,000!")
                                money += 1000
                            else:
                                print()
                                print("Better luck next time")
                        else:
                            print("Better luck next time!")
                elif choice == "b":
                    if money < 500:
                        print()
                        print("You have an insufficient balance.")
                        done = True
                    else:
                        money -= 500
                        slot_one = random.randrange(3)
                        slot_two = random.randrange(3)
                        slot_three = random.randrange(5)
                        if slot_one == slot_two and slot_one == slot_three:
                            if random.randrange(10) == 5:
                                print()
                                print("You won the $20,000 jackpot!")
                                money += 20000
                                done = True
                            else:
                                print()
                                print("You won $9,000!")
                                money += 9000
                        else:
                            if slot_one == slot_two or slot_one == slot_three or slot_two == slot_three:
                                if random.randrange(7) == 0:
                                    print()
                                    print("You won $2,000!")
                                    money += 2000
                                else:
                                    print()
                                    print("Better luck next time")
                            else:
                                print("Better luck next time!")
        if money >= 20000:
            done = True
            print()
            print("You have paid off your debt!")
            print("You Win!")
    return money


main()

