from tkinter import *

window = Tk()
window.title("Wordle")
window.geometry("550x500")
window.configure(bg = "black")

word = "balls"
wordlist = list(word)

i = 1
tries = 1

def true():
    for j in range(5):
            if guesslist[q] == wordlist[j]:
                return True
                break

def Guessgetter(entry):

    global q
    global guesslist
    global guess
    global yaxis

    q = 0
    yaxis = 0
    guess = entry.get()
    guesslist = list(guess)
    print(guess)

    while q < 5:
        if guesslist[q] == wordlist[q]:
            label1 = Label (text = (guesslist[q]), bg = "black", fg = "green")
            label1.grid(row = i-1, column = q+3)
            print(guesslist[q], end = ' ')
        elif true() == True:
            label1 = Label (text = (guesslist[q]), bg = "black", fg = "yellow")
            label1.grid(row = i-1, column = q+3)
            print(guesslist[q], end = ' ')
        else:
            label1 = Label (text = (guesslist[q]), bg = "black", fg = "white")
            label1.grid(row = i-1, column = q+3)
            print(guesslist[q], end = ' ')
        q += 1
        yaxis += 5


    if word == guess:
        return None
    elif tries == 6:
        label1 = Label (text = ("you ran out of tries :("))
        label1.grid(row = i + 5, column = i +7, sticky = S + E)
        
        button1.destroy()
        
    else:
        button1.destroy()

        alternator()
        

def alternator():

    global i
    global tries
    
    global entry1
    entry1 = Entry (bg = "dark gray")
    entry1.insert(END, "")
    entry1.grid(row = i, column = 1)

    global button1
    button1 = Button (text = "Guess", bg = "dark gray", command = lambda: (Guessgetter(entry1)))
    button1.grid(row = i, column = 2, sticky = N + S + E + W)

    tries += 1
    i += 2

alternator()


