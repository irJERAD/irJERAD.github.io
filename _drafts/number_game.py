## Part 1
# generate random number between 1 and 10 inclusive
# get a number guess from the player
# compare guess to secret number
# print out hit/miss

## Part 2
# limit the number of guesses
# catch when someone submits a non-integer
# print "too low" or "too high" message for bad guesses
# let people play again

import random

def game():
    # generate a random number between 1 and 10, inclusive
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        # get a number guess from the player
        guess = input("Guess a number between 1 and 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print("{} isn't an integer!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}.".format(guess))
        guesses.append(guess)
    # elses for while run whenever while finishes on its own
    ## As long as break or exception don't happen, the else will happen
    else:
        print("You didn't get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    # by using lower function we catch N and n
    #### TODO be able to accept all permutations of y,yes,n,no by stripping first letter
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()
