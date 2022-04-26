# Written by Zayne

from tkinter import *
from enchant import Dict
import urllib.request

dictionary = Dict("en_US")

import random

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
    # 1st row
    # q
    img = PhotoImage(file="images/q.gif")
    button = Button(bg="white", image=img,
                    borderwidth=0, highlightthickness=0,
                    activebackground="white", command=lambda:
                    (process("q")))
    button.image = img
    button.grid(row=3, column=0, sticky=N+S+E+W)
    # w
    img = PhotoImage(file="images/w.gif")
    button = Button(bg="white", image=img,
                    borderwidth=0, highlightthickness=0,
                    activebackground="white", command=lambda:
                process("w"))
    button.image = img
    button.grid(row=3, column=1, sticky=N+S+E+W)

    # e
    img = PhotoImage(file="images/e.gif")
    button = Button(bg="white", image=img,
                    borderwidth=0, highlightthickness=0,
                    activebackground="white", command=lambda:
                process("e"))
    button.image = img
    button.grid(row=3, column=2, sticky=N+S+E+W)

    # r
    img = PhotoImage(file="images/r.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    (process("r")))
    button.image = img
    button.grid(row=3, column=3, sticky=N+S+E+W)

    #t
    img = PhotoImage(file="images/t.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("t"))
    button.image = img
    button.grid(row=3, column=4, sticky=N+S+E+W)

    #y
    img = PhotoImage(file="images/y.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("y"))
    button.image = img
    button.grid(row=3, column=5, sticky=N+S+E+W)

    #u
    img = PhotoImage(file="images/u.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("u"))
    button.image = img
    button.grid(row=3, column=6, sticky=N+S+E+W)

    #i
    img = PhotoImage(file="images/i.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("i"))
    button.image = img
    button.grid(row=3, column=7, sticky=N+S+E+W)

    #o
    img = PhotoImage(file="images/o.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("o"))
    button.image = img
    button.grid(row=3, column=8, sticky=N+S+E+W)

    #p
    img = PhotoImage(file="images/p.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("p"))
    button.image = img
    button.grid(row=3, column=9, sticky=N+S+E+W)

    #backspace
    img = PhotoImage(file="images/backspace.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("back"))
    button.image = img
    button.grid(row=3, column=10, sticky=N+S+E+W)

    #2nd row

    #a
    img = PhotoImage(file="images/a.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("a"))
    button.image = img
    button.grid(row=4, column=0, sticky=N+S+E+W)

    #s
    img = PhotoImage(file="images/s.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                        process("s"))
    button.image = img
    button.grid(row=4, column=1, sticky=N+S+E+W)

    #d
    img = PhotoImage(file="images/d.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("d"))
    button.image = img
    button.grid(row=4, column=2, sticky=N+S+E+W)

    #f
    img = PhotoImage(file="images/f.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("f"))
    button.image = img
    button.grid(row=4, column=3, sticky=N+S+E+W)

    #g
    img = PhotoImage(file="images/g.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("g"))
    button.image = img
    button.grid(row=4, column=4, sticky=N+S+E+W)

    #h
    img = PhotoImage(file="images/h.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("h"))
    button.image = img
    button.grid(row=4, column=5, sticky=N+S+E+W)

    #j
    img = PhotoImage(file="images/j.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("j"))
    button.image = img
    button.grid(row=4, column=6, sticky=N+S+E+W)

    #k
    img = PhotoImage(file="images/k.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("k"))
    button.image = img
    button.grid(row=4, column=7, sticky=N+S+E+W)

    #l
    img = PhotoImage(file="images/l.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("l"))
    button.image = img
    button.grid(row=4, column=8, sticky=N+S+E+W)

    #enter
    img = PhotoImage(file="images/enter.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command= lambda: test())
    button.image = img
    button.grid(row=4, column=9, sticky=N+S+E+W)

    #3rd Row

    # z
    img = PhotoImage(file="images/z.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("z"))
    button.image = img
    button.grid(row=5, column=1, sticky=N+S+E+W)

    # x
    img = PhotoImage(file="images/x.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("x"))
    button.image = img
    button.grid(row=5, column=2, sticky=N+S+E+W)

    # c
    img = PhotoImage(file="images/c.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("c"))
    button.image = img
    button.grid(row=5, column=3, sticky=N+S+E+W)
    # v
    img = PhotoImage(file="images/v.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("v"))
    button.image = img
    button.grid(row=5, column=4, sticky=N+S+E+W)

    # b
    img = PhotoImage(file="images/b.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("b"))
    button.image = img
    button.grid(row=5, column=5, sticky=N+S+E+W)

    # n
    img = PhotoImage(file="images/n.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("n"))
    button.image = img
    button.grid(row=5, column=6, sticky=N+S+E+W)

    # m
    img = PhotoImage(file="images/m.gif")
    button = Button(bg="white", image=img,
                        borderwidth=0, highlightthickness=0,
                        activebackground="white", command=lambda:
                    process("m"))
    button.image = img
    button.grid(row=5, column=7, sticky=N+S+E+W)

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

    q = 0

    while q < 5:

        print ("none")

        # for green letters
        #if guesslist[q] == wordlist[q]:

            #label1 = Label(text=(guesslist[q]), bg="dark gray", fg="green")
            #label1.grid(row=i, column=q + 3)

        # for yellow letters, refers to true() for calculations
        #elif true() == True:

            #label1 = Label(text=(guesslist[q]), bg="dark gray", fg="yellow")
            #label1.grid(row=i, column=q + 3)

        # grey letters
        #else:


            #label1 = Label(text=(guesslist[q]), bg="dark gray", fg="black")
            #label1.grid(row=i, column=q + 3)

        # selects next letter
        q += 1

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

##################################################################
######IF YOU WANT THE WORD TO BE RANDOM THEN MAKE IT TRUE######

######THE WORD YOU ARE GUESSING #####

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