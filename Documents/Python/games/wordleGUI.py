from tkinter import *

window = Tk()
window.title("Wordle")
window.geometry("550x500")
window.configure(bg = "black")

######THE WORD YOU ARE GUESSING#####
word = "balls"
wordlist = list(word)

# i is for the entry bars, as i increases the bars go down two columns
i = 1

#tries
tries = 1

#calculates the placement of yellow letters
def true():
    for j in range(5):
            if guesslist[q] == wordlist[j]:
                return True
                break

#the main game
def Guessgetter(entry):

    #globals
    global q
    global guesslist
    global guess

    q = 0

    #takes the input from the entry and assigns it as your guess
    guess = entry.get()
    #turns your guess into a list
    guesslist = list(guess)
    #prints guess for debug
    print(guess)

    while q < 5:
        #for green letters
        if guesslist[q] == wordlist[q]:
            label1 = Label (text = (guesslist[q]), bg = "black", fg = "green")
            label1.grid(row = i-1, column = q+3)
            print(guesslist[q], end = ' ')
        #for yellow letters, refers to true() for calculations
        elif true() == True:
            label1 = Label (text = (guesslist[q]), bg = "black", fg = "yellow")
            label1.grid(row = i-1, column = q+3)
            print(guesslist[q], end = ' ')
        #grey letters
        else:
            label1 = Label (text = (guesslist[q]), bg = "black", fg = "white")
            label1.grid(row = i-1, column = q+3)
            print(guesslist[q], end = ' ')
        q += 1

    #if you guess the word
    if word == guess:
        button1.destroy()
    #if you run out of tries
    elif tries == 6:
        label1 = Label (text = ("you ran out of tries :("))
        label1.grid(row = i + 5, column = i +7, sticky = S + E)
        
        button1.destroy()
    #if you are still playing; deletes the guess button and creates a new guess button and entry bar
    else:
        #deletes guessbutton
        button1.destroy()

        alternator()
        
#the actual entry bar and guess
def alternator():

    #globals
    global i
    global tries
    
    global entry1
    entry1 = Entry (bg = "dark gray")
    entry1.insert(END, "")
    entry1.grid(row = i, column = 1)

    global button1
    button1 = Button (text = "Guess", bg = "dark gray", command = lambda: (Guessgetter(entry1)))
    button1.grid(row = i, column = 2, sticky = N + S + E + W)

    #increases tries
    tries += 1
    #increases column
    i += 2

alternator()


