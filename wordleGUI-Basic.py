# Techle written by Zayne and Ruth, LED support written by Michael

from tkinter import *
from enchant import Dict
import urllib.request
import RPi.GPIO as GPIO
import random

dictionary = Dict("en_US")

############################################################################################################

# creates the frame
def frame():
    global window

    window = Tk()
    window.title("Techle")
    window.geometry("1300x450")
    window.configure(bg="white")

    global label1
    
    label1 = Label (text = "", bg="white", font = ("Times New Roman", 20))
    label1.grid(row=0, rowspan = 2, column=0, sticky=N + S + E + W)
    
    keyboard()
    scroller()
    
######################################################################

def keyboard():
#Keyboard
    # 1st row letters list
    firstRowList = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "backspace"]
    # initializes first row of keyboard
    for i in range(len(firstRowList)):
        img = PhotoImage(file=f"images/{firstRowList[i]}.gif")
        button = Button(bg="white", image=img,
                    borderwidth=0, highlightthickness=0,
                    activebackground="white", command=lambda:
                    (process(f"{firstRowList[i]}")))
        button.image = img
        button.grid(row=3, column=i, sticky=N+S+E+W)
    
    #2nd row letters list
    secondRowList = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "enter"]
    # initializes 2nd row of keyboard
    for i in range(len(secondRowList)):

        img = PhotoImage(file=f"images/{secondRowList[i]}.gif")
        button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process(f"{secondRowList[i]}"))
        button.image = img
        button.grid(row=4, column=i, sticky=N+S+E+W)
        
    #3rd row letters list
    thirdRowList = ["z", "x", "c", "v", "b", "n", "m"]
    # initializes 3rd row of keyboard
    for i in range(len(thirdRowList)):
        img = PhotoImage(file=f"images/{thirdRowList[i]}.gif")
        button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process(f"{thirdRowList[i]}"))
        button.image = img
        button.grid(row=5, column=i+1, sticky=N+S+E+W)
                        
#takes the input of buttons
def process(button):
    
    if button == "back":
        display = label1["text"]
        backtext = (display)[:-1]
        label1["text"] = backtext
    else:
        label1["text"] += button

def randomwordgen():
    # globals
    global ranword
    global wordlist
    global word

    # chooses a random word from the list of 10000 words
    ranword = random.choice(words)

    # makes sure the word is 5 letters
    while len(ranword) > 5 or len(ranword) < 5 or dictionary.check(ranword) == False:
        ranword = random.choice(words)
        word = ranword
        wordlist = list(word)
        print(word)
        
###############################################################################
def test():
    # globals
    global guesslist
    global guess

    # takes the input from the entry and assigns it as your guess
    guess = label1["text"]

    # turns your guess into a list
    guesslist = list(guess)

    # if the left of your guess is not 5 letters or a real word
    if len(guesslist) > 5 or len(guesslist) < 5 or dictionary.check(guess) == False:

        global label2

        label2 = Label(text="Your guess has to be 5 letters long and a real word.",
                       bg="dark gray", fg="black", bd = 10, font=("Times New Roman", 30))
        label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # after 3 seconds destroy the label
        window.after(3000, destroy_label)

    else:
        Guessgetter(label1)

#destroys the warning label
def destroy_label():
    label2.destroy()

##################################################################
i = 1
tries = 1
j = 1
# the main game
def Guessgetter(entry):
    # globals
    global i
    global tries
    global q
    
    # Resets LEDs before displaying new pattern
    for a in range(len(blue)):  # len(blue) as all LED lists are the same length
        greenLight(green[a], False)
        yellowLight(red[a], green[a], False)
        whiteLight(red[a], green[a], blue[a], False)

    for q in range(0,5):
        print ("none")
    
        # for green letters
        if guesslist[q] == wordlist[q]:
            greenLight(green[q], True)

        # for yellow letters, refers to true() for calculations
        elif true() == True:
            yellowLight(red[q], green[q], True)

        # grey letters
        else:
            whiteLight(red[q], green[q], blue[q], True)

    # increases column
    i += 2

    # increases tries
    tries += 1

    # if you guess the word
    if word == guess:

        Button2 = Button(text=("You got the word!. Click to play again."),
                         bg="dark gray", fg="black", bd = 10, font=("Times New Roman", 30), command=lambda: destroyfunction())
        Button2.place(relx=0.5, rely=0.5, anchor=CENTER)

    # if you run out of tries
    if tries == 7:

        Button2 = Button(text=("You ran out of tries. The word was {}. Click to try another word."
                               .format(word)),
                         bg="dark gray", fg="black", bd = 10, font=("Times New Roman", 30), command=lambda: destroyfunction())
        Button2.place(relx=0.5, rely=0.5, anchor=CENTER)

    global j
    
    label4["text"] += (guess + ' | ')

##################################################################
#makes the scroll wheel of your guesses
def scroller():
    global label4
    
    label4 = Label(bg = "white", fg ="black", font=("Times New Roman", 30))
    label4.grid(row = 2, columnspan = 10)

    label4["text"] += '| '
        

#########################################################################
# calculates the placement of yellow letters
def true():
    for j in range(5):
        if guesslist[q] == wordlist[j]:
            return True
            break

def destroyfunction():
    # globals
    global i
    global tries

    # resets the tries and columns
    i = 1
    tries = 1

    # destroys window
    window.destroy()

    # chooses new word
    randomwordgen()

    # creates new window
    frame()


# LED functions for yellow, green, and white lights
##################################################################

def  yellowLight(red, green, boolean):
    GPIO.output(red, boolean)
    GPIO.output(green, boolean)

def greenLight(green, boolean):
    GPIO.output(green, boolean)

def whiteLight(red, green, blue, boolean):
    GPIO.output(red, boolean)
    GPIO.output(green, boolean)
    GPIO.output(blue, boolean)

##################################################################
######IF YOU WANT THE WORD TO BE RANDOM THEN MAKE IT TRUE######

######THE WORD YOU ARE GUESSING #####

# GPIO Initialization
GPIO.setmode(GPIO.BCM)

red = [5, 6, 12, 13, 16]
green = [17, 18, 19, 20, 21]
blue = [22, 23, 24, 25, 26]

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# url that has 10000 random words
word_url = "https://www.mit.edu/~ecprice/wordlist.10000"

# opens the url
response = urllib.request.urlopen(word_url)

# makes it a sentence in python
long_txt = response.read().decode()

# makes it a list
words = long_txt.splitlines()

randomword = True

if randomword == True:
    randomwordgen()
else:
    #MUST BE 5 LETTERS AND REAL
    word = ""

frame()

GPIO.cleanup()
