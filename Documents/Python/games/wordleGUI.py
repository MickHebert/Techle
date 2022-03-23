from tkinter import *
from enchant import Dict
import urllib.request

dictionary = Dict("en_US")

import random

def randomwordgen():
    
    #globals
    global ranword
    global wordlist
    global word

    #chooses a random word from the list of 10000 words
    ranword = random.choice(words)
    
    #makes sure the word is 5 letters
    while len(ranword) > 5 or len(ranword) < 5 or dictionary.check(ranword) ==False:
        
        ranword = random.choice(words)
        word = ranword
        wordlist = list(word)
        print(word)

############################################################################################################

# i is for the entry bars, as i increases the bars go down two columns
i = 1

#tries
tries = 1

#destroys the frame
def destroyfunction():
    
    #globals
    global i
    global tries
    
    #resets the tries and columns
    i = 1
    tries = 1

    #destroys window
    window.destroy()

    #chooses new word
    randomwordgen()

    #creates new window
    frame()
    
#creates the frame
def frame():

    global window

    window = Tk()
    window.title("Wordle")
    window.geometry("500x500")
    window.configure(bg = "dark gray")
    
    alternator()

    window.mainloop()

############################################################################################################

#the actual entry bar and guess
def alternator():
    
    global entry1
    
    entry1 = Entry (bg = "dark gray")
    entry1.insert(END, "")
    entry1.grid(row = i, column = 0, sticky = N+S+E+W)

    global button1
    
    button1 = Button (text = "Guess", bg = "dark gray", command = lambda: (test()))
    button1.grid(row = i, column = 1, sticky = N +S+E + W)
    

#the main game
def Guessgetter(entry):

    #globals
    global i
    global tries
    global q

    q = 0

    while q < 5:
        #for green letters
        if guesslist[q] == wordlist[q]:
            
            label1 = Label (text = (guesslist[q]), bg = "dark gray", fg = "green")
            label1.grid(row = i, column = q+3)
            
        #for yellow letters, refers to true() for calculations
        elif true() == True:
            
            label1 = Label (text = (guesslist[q]), bg = "dark gray", fg = "yellow")
            label1.grid(row = i, column = q+3)
            
        #grey letters
        else:
            
            label1 = Label (text = (guesslist[q]), bg = "dark gray", fg = "black")
            label1.grid(row = i, column = q+3)

        #selects next letter
        q += 1

    #increases column
    i += 2

    #increases tries
    tries += 1
    

    #if you guess the word
    if word == guess:
        
        button1.destroy()
        
        Button2 = Button (text = ("You got the word!. Click to play again."),
                          bg = "dark gray", fg = "black", command = lambda:destroyfunction())
        Button2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    #if you run out of tries
    elif tries == 7:
        
        Button2 = Button (text = ("You ran out of tries. The word was {}. Click to try another word."
                                  .format(word)),
                          bg = "dark gray", fg = "black", command = lambda:destroyfunction())
        Button2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        button1.destroy()

    #if you are still playing; deletes the guess button and creates a new guess button and entry bar
    else:
        #deletes guessbutton
        button1.destroy()

        alternator()

############################################################################################################

#calculates the placement of yellow letters
def true():
    for j in range(5):
            if guesslist[q] == wordlist[j]:
                return True
                break

#destroys the label in test() after 3 seconds
def destroy_label():
    label2.destroy()

#tests the word to make sure it is real and 5 letters
def test():

    #globals
    global guesslist
    global guess
    
    #takes the input from the entry and assigns it as your guess
    guess = entry1.get()

    #turns your guess into a list
    guesslist = list(guess)

    #if the left of your guess is not 5 letters or a real word
    if len(guesslist) > 5 or len(guesslist) < 5 or dictionary.check(guess) == False:

        global label2

        label2 = Label (text = "Your guess has to be 5 letters long and a real word.", bg = "dark gray", fg = "black")
        label2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        #after 3 seconds destroy the label
        window.after(3000, destroy_label)
        
        button1.destroy()
        entry1.destroy()
        alternator()

    else:
       Guessgetter(entry1)

############################################################################################################
######IF YOU WANT THE WORD TO BE RANDOM THEN MAKE IT TRUE######

######THE WORD YOU ARE GUESSING #####

#url that has 10000 random words
word_url = "https://www.mit.edu/~ecprice/wordlist.10000"

#opens the url
response = urllib.request.urlopen(word_url)

#makes it a sentence in python
long_txt = response.read().decode()

#makes it a list
words = long_txt.splitlines()

randomword = True

if randomword == True:
    randomwordgen()
else:
    word = ""
frame()
