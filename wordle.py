######################################################################################################################
### Name: Zayne, Ruth, Michael
### Date: 3/21/2022
### Program: Wordle Game
### Written by Zayne
######################################################################################################################

from colorama import Fore, Back, Style

from enchant import Dict

dictionary = Dict("en_US")

##############THE WORD YOU ARE GUESSING################
word = "their"
#######################################################

# The sentences are variables because i need the \n
guesstence = "\nWhat is your guess?   "
losingtence = "\nYou ran out of tries, boohoo loser.   "
winningtence = "\nGenius!   "

# makes the wordle a list
wordlist = (list(word))

torf = False


# the main function
def nextguess():
    # globals the variables for the true() function
    global i
    global guess
    global guesslist

    # makes your guess a str list
    guess = str(input(guesstence))
    guesslist = list(guess)

    # youur number of tries and the letter specified for the yellows
    i = 0

    # keeps the word at 5 letters and a real word
    while (5 < len(guess)) or (len(guess) < 5) or (dictionary.check(guess) == False):
        print("Your guess can be only 5 letters and a real word.")
        guess = str(input("What is your actual guess?   "))
        guesslist = list(guess)

    while i < 5:
        if guesslist[i] == wordlist[i]:
            print(Fore.GREEN + guesslist[i] + Style.RESET_ALL, end=' ')
        elif true() == True:
            print(Fore.YELLOW + guesslist[i] + Style.RESET_ALL, end=' ')
        else:
            print(guesslist[i] + Style.RESET_ALL, end=' ')
        i += 1


# for the yellow letters
def true():
    for j in range(5):
        if guesslist[i] == wordlist[j]:
            return True
            break


# initiates the game
def model():
    # don't know why i have to global this variable but it doesnt work otherwise
    global torf

    # uses the function 6 times
    for p in range(5):

        # when you win
        if guess == word:
            torf = True
            print(winningtence)
            break

        nextguess()

    # When you lose, or more specifically, run out of tries
    if torf == False:
        print(losingtence)


nextguess()
model()