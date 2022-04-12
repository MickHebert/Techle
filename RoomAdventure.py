#################################################################
# Names: Ruth Anderson, Zayne Randall, Michael Hebert
# Date: 04/11/2022
# Description: Pi Activity 1
#################################################################
from tkinter import *

# Game Story: You are on a search for grandpa's treasure after his death.
# To Win: look apron, look pocket, take paper, read paper, go east (library),
# read green_book, take key, go west, go south (study), look statue, go down, use key

# the room class
class Room:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    def addExit(self, exit, room):
        self._exits[exit] = room

    def addItem(self, item, desc):
        self._items[item] = desc

    def addGrabbable(self, item):
        self._grabbables.append(item)

    def delGrabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
        # the room name
        s = "You are in {}.\n".format(self.name)
        # items in the room
        s += "You see: "

        for item in self.items.keys():
            s += item + " "
        s += "\n"
        # exits from the room
        s += "Exits: "

        for exit in self.exits.keys():
            s += exit + " "

        return s


# the game class
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        global r4
        r1 = Room("the kitchen", "images/room1.gif")
        r2 = Room("the library", "images/room2.gif")
        r3 = Room("the study", "images/room3.gif")
        r4 = Room("the basement", "images/room4.gif")

        # add exits to room 1
        r1.addExit("east", r2)  # to the east of room 1 is room 2
        r1.addExit("south", r3)
        # add grabbables to room 1
        r1.addGrabbable("paper")
        # add items to room 1
        r1.addItem("apron",
                   "The apron is covered in stains, someone must have cooked a lot with this. There is a something in  the pocket.")
        r1.addItem("pocket", "The pocket contains a crumpled piece of paper.")
        r1.addItem("oven", "It is black and rusty.")
        # add exits to room 2
        r2.addExit("west", r1)
        # r2.addExit("south", r4)  # as there is only one entrance into most basements, the south exit for room 2 has been removed
        # add grabbables to room 2
        r2.addGrabbable("red_book")
        r2.addGrabbable("green_book")
        r2.addGrabbable("blue_book")
        r2.addGrabbable("key")
        # add items to room 2
        # the green book is the book with the key inside
        r2.addItem("green_book", "It is very dusty. Maybe you could read it?")
        r2.addItem("red_book", "It has a gold symbol on the front. \nIt is very beautiful. Maybe you could read it?")
        r2.addItem("blue_book", "It has a silver symbol on it. Maybe you could read it?")
        r2.addItem("fireplace", "It is full of ashes.")

        # add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("down", r4)
        # add grabbables to room 3
        r3.addGrabbable("statue")
        # add items to room 3
        r3.addItem("statue", "It is in the likeness of a man on a set of        stairs; he points downwards.")
        r3.addItem("fireplace", "It is full of ashes.")
        # add exits to room 4
        # r4.addExit("northeast", r2)
        r4.addExit("up", r3)  # up since there is a staircase upwards
        r4.addExit("south", None)  # DEATH!
        # add items to room 4
        r4.addItem("door", "It is green and has a keyhole!")
        r4.addItem("pit", "There is a bottomless pit in the room.\nWhat did grandpa need this for?")

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1
        # initialize the player's inventory
        Game.inventory = []

    # sets up the GUI
    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)

        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        text_frame = Frame(self, width=WIDTH // 2)

        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="images/skull.gif")  # THIS WAS MODIFIED BY Zakaria
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # THIS WAS MODIFIED BY Zakaria
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now is   quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + \
                             "\nYou are carrying: " + str(Game.inventory) + \
                             "\n\n" + status)
            Game.text.config(state=DISABLED)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus(
            "You received a cryptic letter from your late      grandfather instructing you to come to his        mansion. " \
            "Unsure of what you will discover, you    venture into the kitchen.")

    def process(self, event):
        action = Game.player_input.get()
        action = action.lower()
        response = "I don't understand. Try verb noun. Valid verbs    are: go, look, use, read, and take"

        if (action == "quit" or action == "exit" or action == "bye" \
                or action == "sionara!"):
            exit(0)

        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        words = action.split()

        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            if (verb == "go"):
                # set a default response
                response = "Invalid exit."
                if (noun in Game.currentRoom.exits):
                    Game.currentRoom = \
                        Game.currentRoom.exits[noun]
                    # set the response (success)
                    response = "Room changed."
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # if one is found, set the response to the item's description
                    response = Game.currentRoom.items[noun]
            # verb is read
            elif (verb == "read"):
                response = "This item cannot be read."
                if (noun == "paper"):
                    # this is a clue instructing the user to go to the library (room 2)
                    response = "Begin your search with the books. "
                elif (noun == "green_book"):
                    response = (
                        "To your amazement, you find the book contains no pages, but a golden key. "
                        "\nPerhaps you should use it on something...")
                elif (noun == "blue_book" or "red_book"):
                    response = ("The words are written in another language that   you cannot understand.")

            # the verb is: use
            elif (verb == "use"):
                response = "This item cannot be used."
                if (Game.currentRoom == r4):
                    if (noun == "key"):
                        response = (
                            "You open the door and see a room full of          treasure! You have made your grandfather proud!"
                            " \nCongratulations!")
                # set a default response
                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        break

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
