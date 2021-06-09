import random
import arcade


def main():
    done = False
    money = 1000
    print()

    # intro
    welcome_sign()

    # questions
    while not done:
        # new line
        print()
        print("Menu")
        print("A. Roulette")
        print("B. Slots")
        print("C. Russian roulette")
        print("D. Check balance")
        print("E. Quit")
        # answering each question
        choice = input("Your choice? ").lower()
        if choice == "e":
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
            money = russian_roulette(money)
            if money < 0:
                done = True
        elif choice == "d":
            print("Balance: $", money)

        if money >= 20000:
            print("Game over!")
            done = True


def russian_roulette(money):
    # Russian roulette description

    print()
    print("Welcome to Russian roulette.")
    print()
    print("Spin the barrel of a loaded gun, point it at yourself, and fire.")
    print("There are 6 spots for bullets in the barrel, and one bullet.")
    print("It will fire 5 times, and if you don't die then you get a $20,000 jackpot.")
    print("If you fire the bullet, then you will die and the game will be over.")
    print("Entry is free.")

    print()
    print("Russian roulette:")
    print("A. Spin barrel and shoot")
    print("B. Menu")
    choice = input("Your choice? ").lower()
    # Russian roulette code

    died = False

    if choice == "b":
        print()

    elif choice == "a":
        for i in range(5):
            print("Fired round: ", i+1)
            gun_barrel = random.randrange(6)

            # bullet is in slot number 3
            if gun_barrel == 3:
                died = True
                print()
                print("You have died.")
                print("Game Over.")

                # come out of the for loop
                break

        if not died:
            money += 20000
        else:
            money -= 20000

    else:
        print()
        print("Invalid choice")

    if not died and money >= 20000:
        print()
        print("You have paid off your debt!")
        print("You Win!")

    return money


def roulette(money):
    # roulette description
    print()
    print("Welcome to roulette!")
    print("Place a bet on a specific number or category.")
    print("After the ball is thrown, you will make a certain amount of money depending on what number it lands on.")

    # roulette code
    done = False
    while not done:
        print()
        print("Roulette:")
        print("A. Place bets")
        print("B. Check balance")
        print("C. Menu")
        choice = input("Your choice? ").lower()

        if choice == "c":
            done = True
            print()

        elif choice == "b":
            print("Balance: $", money)

        elif choice == "a":
            valid_input = False
            roulette_bet = 0
            while not valid_input:
                print()
                print("How much money would you like to bet this session?")
                print("You can bet up to your current balance: $", money)
                roulette_bet = input("$")
                if roulette_bet.strip().isdigit():
                    roulette_bet = int(roulette_bet.strip())
                    print()
                    if roulette_bet > money:
                        print("Insufficient funds.")
                    else:
                        valid_input = True

                else:
                    print()
                    print("Invalid input.")

            money -= roulette_bet

            # throw ball
            ball = random.randrange(37)

            print("Type of bets:")
            print("A. Specific numbers")
            print("B. Even or odd number")
            choice = input("Your choice? ").lower()
            if choice == "a":
                print()
                print("Number choices include 0, 1, 2, 3...36")
                print("You can bet on up to 4 numbers")
                print()
                number_1 = input("1st number: ")
                number_2 = input("2nd number: ")
                number_3 = input("3rd number: ")
                number_4 = input("4th number: ")
                if number_1.strip().isdigit() and number_2.strip().isdigit() and number_3.strip().isdigit() and number_4.strip().isdigit():

                    # as a casino I would put a multiplier of less than 9, but I want the user to win.
                    winning = 12 * roulette_bet

                    my_winning = 0
                    number_4 = int(number_4)
                    number_3 = int(number_3)
                    number_2 = int(number_2)
                    number_1 = int(number_1)

                    # check whether user has won
                    if ball == number_1:
                        my_winning += winning
                    if ball == number_2:
                        my_winning += winning
                    if ball == number_3:
                        my_winning += winning
                    if ball == number_4:
                        my_winning += winning

                    print()
                    print("The ball landed on", ball, ".")
                    if my_winning > 0:
                        print()
                        print("Congratulations, you won $", my_winning, ".")
                        money += my_winning
                    else:
                        print()
                        print("Better luck next time.")
                else:
                    print()
                    print("Invalid input.\n")
            else:
                # odd or even bet
                print()
                print("Would you like to bet on odd or even numbers?")
                print("A. Odd")
                print("B. Even")
                user_choice = input("You choice? ").lower()
                remainder = ball % 2

                print()
                print("The ball landed on", ball, ".")

                if (user_choice == "a" and remainder == 1) or (user_choice == "b" and remainder == 0):
                    # as a casino I would put a multiplier of less than 2, but I want the user to win.
                    my_winning = 2 * roulette_bet
                    print()
                    print("Congratulations, you won $", my_winning, ".")
                    money += my_winning
                else:
                    print()
                    print("Better luck next time")

        if money >= 20000:
            done = True
            print()
            print("You have paid off your debt!")
            print("You Win!")
        if money <= 0:
            print()
            print("You have run out of money.")
            print("You have two choices:")
            print("A. Russian roulette")
            print("B. Quit")
            choice = input("Your choice? ").lower()
            if choice == "b":
                done = True
                print()
            if choice == "a":
                russian_roulette(money)
                done = True

    return money


def slots(money):
    # slots disc.
    print()
    print("Welcome to slots!")
    print("Spin to win! Spend more money to earn better prizes!")
    # slots code

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
                print("You need at least $200 to play slots.")
                print("Current balance: $", money)
                done = True
            else:
                print()

                print("A. Spend 200 dollars")
                print("B. Spend 500 dollars")
                print("C. Menu")
                choice = input("Your choice? ").lower()
                if choice == "c":
                    done = True
                    print()
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
                        print("You need at least $500.")
                        print("Current balance: $", money)
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
        if money <= 0:
            print()
            print("You have run out of money.")
            print("You have two choices:")
            print("A. Russian roulette")
            print("B. Quit")
            choice = input("Your choice? ").lower()
            if choice == "b":
                done = True
                print()
            if choice == "a":
                russian_roulette(money)
                done = True
    return money


def welcome_sign():
    # Graphic welcome sign

    arcade.open_window(900, 900, "Casino Welcome Sign")

    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
    arcade.start_render()

    arcade.draw_lrtb_rectangle_filled(240, 660, 460, 250, arcade.csscolor.LIGHT_STEEL_BLUE)
    arcade.draw_lrtb_rectangle_outline(240, 660, 460, 250, arcade.csscolor.BLACK, 4)

    arcade.draw_text("Welcome to The Casino Game!",
                     295, 410,
                     arcade.color.BLACK, 20,)
    arcade.draw_text("You are in debt for $20,000. Your goal",
                     255, 380,
                     arcade.color.BLACK, 20,)
    arcade.draw_text(" is to make this $20,000 in the casino ",
                     255, 350,
                     arcade.color.BLACK, 20,)
    arcade.draw_text(" with $1,000. Failure to acquire this ",
                     255, 320,
                     arcade.color.BLACK, 20,)
    arcade.draw_text("money will result in debt collectors ",
                     255, 290,
                     arcade.color.BLACK, 20,)
    arcade.draw_text(" arresting you.",
                     255, 260,
                     arcade.color.BLACK, 20,)
    arcade.draw_text("Close this Window to Start Playing",
                     330, 200,
                     arcade.color.RED, 14, )

    arcade.draw_lrtb_rectangle_filled(320, 335, 600, 462, arcade.csscolor.GRAY)
    arcade.draw_lrtb_rectangle_filled(560, 575, 600, 462, arcade.csscolor.GRAY)

    arcade.draw_lrtb_rectangle_filled(280, 310, 248, 80, arcade.csscolor.GRAY)
    arcade.draw_lrtb_rectangle_filled(590, 620, 248, 80, arcade.csscolor.GRAY)

    arcade.draw_text("$",
                     310, 370,
                     arcade.color.BLACK, 420,)
    arcade.draw_text("$",
                     320, 390,
                     arcade.color.FOREST_GREEN, 400,)

    arcade.draw_lrtb_rectangle_filled(350, 360, 680, 670, arcade.csscolor.GRAY)
    arcade.draw_lrtb_rectangle_filled(540, 550, 680, 670, arcade.csscolor.GRAY)

    arcade.draw_lrtb_rectangle_filled(200, 700, 760, 680, arcade.csscolor.LIGHT_STEEL_BLUE)
    arcade.draw_lrtb_rectangle_outline(200, 700, 760, 680, arcade.csscolor.BLACK, 4)

    arcade.draw_lrtb_rectangle_filled(300, 600, 670, 600, arcade.csscolor.LIGHT_STEEL_BLUE)
    arcade.draw_lrtb_rectangle_outline(300, 600, 670, 600, arcade.csscolor.BLACK, 4)

    arcade.draw_text("Welcome to",
                     265, 680,
                     arcade.color.BLACK, 60,)
    arcade.draw_text("The Casino",
                     340, 606,
                     arcade.color.BLACK, 40,)

    arcade.draw_ellipse_filled(450, -300, 1900, 800, arcade.csscolor.DARK_GREEN)

    arcade.finish_render()

    arcade.run()


main()
