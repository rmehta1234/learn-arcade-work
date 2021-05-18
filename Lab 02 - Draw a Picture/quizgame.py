# variables to track percentage of correct answers
final_score = 0
total_questions = 5

print()

# question 1
users_answer = input("""An organism's reproductive cells are called...?
? """)
if users_answer.lower() == "gametes":
    print("That is correct.")
    final_score += 1
else:
    print("Wrong. The correct answer is gametes.")

print()

# question 2
users_answer = input("What was the original name for Google?"
"""
1. Confinity
2. America Online
3. BackRub
4. LemonSearch
? """)
if users_answer.upper() == "BACKRUB" or (users_answer.strip().isdigit() and int(users_answer) == 3):
    print("Correct")
    final_score += 1
else:
    print("Incorrect. The correct answer is BackRub.")

print()

# question 3
users_answer = input("Which Disney princess sings Someday My Prince Will Come ?"
"""
1. Cinderella
2. Snow White
3. Belle
4. Aurora
? """)
if users_answer.upper() == "SNOW WHITE" or (users_answer.strip().isdigit() and int(users_answer) == 2):
    print("Correct")
    final_score += 1
else:
    print("Incorrect. The correct answer is Snow White.")

print()

# question 4
users_answer = input("""What starts with an E, and ends with an E, but only has one letter in it.
? """)
if users_answer.lower() == "an envelope" or users_answer.lower() == "envelope":
    print("That is correct.")
    final_score += 1
else:
    print("Wrong. The correct answer is, an envelope")

print()

# question 5
users_answer = input("""What is 1+1
? """)
# See if it is a number and 2, if so then convert to integer
if users_answer.strip().isdigit() and int(users_answer) == 2:
    users_answer = int(users_answer)
last_questions_answer = 2
if users_answer == last_questions_answer:
    print("Nice!")
    final_score += 1
else:
    print("You need to go back to elementary school")

print()

# final score summary
percentage = (final_score / total_questions) * 100
if percentage >= 80:
    print("Nice Job. Your final score is", percentage, "%")
else:
    print("Better luck next time. Your score is", percentage, "%")
