from tkinter import *

window = Tk()
window.title("Wordle")
window.geometry("250x400")

def entryword():
    entry1 = Entry (bg = "white")
    entry1.insert(END, "")
    entry1.grid(row = 1, column = 0, sticky = N + S + E + W)

    button1 = Button (text = "Guess", command = lambda: (Guessgetter(entry1)))
    button1.grid(row = 1, column = 2, sticky = N + S + E + W)

def Guessgetter(entry):
    guess = entry.get()
    print(guess)

entryword()
    
