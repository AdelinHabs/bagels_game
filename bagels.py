
# Generate a four-digit code randomly.
# Prompt the user to guess the four-digit code.
# Compare the user's guess to the randomly four-digit code and give him feedback based on his guess.
# The user is to use the feedback to refine his guess until he guesses it right.


from random import randint

print("\n\n                                        !!!!! WELCOME TO THE BAGELS GAME !!!!!!"
      "\n                        A four digit code is to be generated randomly and you are to try and guess it."
      "\nFeedback will be given to you, and you are to use the feedback to refine your guess until you have guessed the four-digit code"
      "\n                                               The maximum number of tries are 10."
      "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~KEYWORDS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      "\n                  \"Correct\"  means the digit is part of the random number and is in it's correct position."
      "\n                  \"Pin\"      means the digit is part of the random number but isn't in it's correct position."
      "\n                  \"Bagel\"    means the digit isn't part of the random number."
      "\n\nFor Example:"
      "\n            The randomly generated four-digit code: 1234"
      "\n            Your guess: 1456"
      "\n            Feedback:   1(Correct), 4(Pin), 5(Bagel), 6(Bagel)"
      "\n            Next guess: 1247 (Using the feedback to refine your next guess)\n\n\n\n")

random_0 = randint(0, 9)
random_1 = randint(0, 9)
random_2 = randint(0, 9)
random_3 = randint(0, 9)
random_number = f"{random_0}{random_1}{random_2}{random_3}"

tries = 0
game = False

while not game:
    if tries >= 10:
        print("\n!!!!!GAME OVER!!!!!, Your 10 tries have all been used. TRY AGAIN, later.")

        should_continue = input("Do you want to try again?.....If yes, type \"Y\", If no, type anything else: ").upper()
        if should_continue == "Y":
            tries = 0
            game = False
        else:
            game = True
    else:
        user_guess = input("Enter your guess: ")
        tries += 1
        if len(user_guess) != 4:
            print("!!!!!!!!!!!!!!!!!!!!!!RETRY and provide a \"FOUR DIGIT\" number!!!!!!!!!!!!!!!!!!!!!!")
            game = False
        else:
            zero_user = user_guess[0]
            first_user = user_guess[1]
            second_user = user_guess[2]
            third_user = user_guess[3]

            # CHECKING WHETHER THE 1ST NUMBER IN USER_GUESS IS IN THE RANDOM NUMBER AND IF IT'S INDEX IN THE RANDOM NUMBER IS EQUAL TO 0
            if zero_user in random_number and zero_user == random_number[0]:
                zero_status = "Correct"
            elif zero_user in random_number and zero_user != random_number[0]:
                zero_status = "Pin"
            else:
                zero_status = "Bagel"

            # CHECKING WHETHER THE 2ND NUMBER IN USER_GUESS IS IN THE RANDOM NUMBER AND IF IT'S INDEX IN THE RANDOM NUMBER IS EQUAL TO 1
            if first_user in random_number and first_user == random_number[1]:
                first_status = "Correct"
            elif first_user in random_number and first_user != random_number[1]:
                first_status = "Pin"
            else:
                first_status = "Bagel"

            # CHECKING WHETHER THE 3RD NUMBER IN USER_GUESS IS IN THE RANDOM NUMBER AND IF IT'S INDEX IN THE RANDOM NUMBER IS EQUAL TO 2
            if second_user in random_number and second_user == random_number[2]:
                second_status = "Correct"
            elif second_user in random_number and second_user != random_number[2]:
                second_status = "Pin"
            else:
                second_status = "Bagel"

            # CHECKING WHETHER THE 4TH NUMBER IN USER_GUESS IS IN THE RANDOM NUMBER AND IF IT'S INDEX IN THE RANDOM NUMBER IS EQUAL TO 3
            if third_user in random_number and third_user == random_number[3]:
                third_status = "Correct"
            elif third_user in random_number and third_user != random_number[3]:
                third_status = "Pin"
            else:
                third_status = "Bagel"


            print(f"{zero_user}({zero_status}), {first_user}({first_status}), {second_user}({second_status}), {third_user}({third_status})")

            if zero_status != "Correct" or first_status != "Correct" or second_status != "Correct" or third_status != "Correct":
                game = False
            else:
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                      f"\n                              !!!!!!!YOU HAVE PASSED!!!!!!!"
                      f"\n                                THE RANDOM NUMBER IS {random_number}"
                      f"\n                              You have done it in {tries} try(s).")
                game = True
