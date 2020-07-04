import CluedoCards
import CluedoCharacters
import CluedoRooms
import CluedoWeapons
from sys import exit
import random
import textwrap
from textwrap import dedent, indent
import time

class earlyFinishes(object):
    #A selection of messages to be given to the user, should they choose not to proceed
    earlyFinishes = ["Well... I guess that's it then. Some investigator you are.",
                     "I suppose that's it then. Bye.",
                     "Where did you go to investigator school? Bye Felicia.",
                     "+1 unsolved murder then. You lose."]

class Room(object):

    def __init__(self, playerCards, NPCCards):
        #set up arguments for passing through player cards and NPC cards, as some rooms need to inherit these values
        self.playerCards = playerCards
        self.NPCCards = NPCCards

    def enter(self):
        #An error message to be displayed in case a room has not been set up properly
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Kitchen(Room):
    pass

class Ballroom(Room):
    pass

class Conservatory(Room):
    pass

class DiningRoom(Room):
    pass

class Cellar(Room):
    pass

class BilliardRoom(Room):
    pass

class Library(Room):
    pass

class Study(Room):
    pass

class Lobby(Room):

    def enter(self):
        #enter the lobby, start the door knock as part of story progression
        print(f"\n.....................................")
        knock = 'KNOCK'
        numKnocks = 3
        start = 0

        print("\n")

        while start < numKnocks:
            print(f"*KNOCK*")
            time.sleep(1)
            start += 1

        time.sleep(1)

        print(f"\nThere's a faint sound of footsteps approaching...")

        time.sleep(3)

        print(f"\nThe person who greets you has clearly seen better days. Aghast, dishevelled, beside themselves.\n")

        time.sleep(5)

        print(f"BUTLER:")

        butlerDialogue = """Oh my - thank God you've arrived! I'm Jeeves, the butler at this fine establishment. There's been a terrible accident. You see, one of our guests... Mr. Body. He's been murdered! It's positively ghastly!\n"""

        print(textwrap.fill(butlerDialogue, 60, initial_indent='        ', subsequent_indent='      '))

        progress = input("\n> Are you ready to start investigating? Y/N\n")

        #options based on user input
        if progress == "Y":
            print(f"\nYou have a private chat with the butler before going any further.\nYou can, with some certainty, rule out the following things:\n{playerCards}")
            print(f"\nYou'll probably want to keep a note of these. They're your cards.")
            nextScene = Hallway(playerCards, NPCCards)
            nextScene.enter()
        elif progress == "N":
            #call the list of early finish options, declared at the start of the code
            quip = earlyFinishes()
            quip = quip.earlyFinishes[random.randint(0,len(quip.earlyFinishes)-1)]
            print(f"{quip}")
        else:
            print("That doesn't look quite right. Type Y or N")
            progress = input("> Are you ready to start investigating? Y/N\n")
            if progress == "Y":
                print(f"\nYou have a private chat with the butler before going any further.\nYou can, with some certainty, rule out the following things:\n{playerCards}")
                print(f"\nYou'll probably want to keep a note of these. They're your cards.")
                nextScene = Hallway(playerCards, NPCCards)
                nextScene.enter()
            else:
                quip = earlyFinishes()
                quip = quip.earlyFinishes[random.randint(0,len(quip.earlyFinishes)-1)]
                print(f"{quip}")

class Hallway(Room):

    def enter(self):
        print(f"\n.....................................\n")

        hallwayIntros = ["The hallways are eerily silent, aside from the faint whispers of the guests. You have a job to do though, so you're pushing on.\n",
                         "You head to the hallway of the manor. The whole place is stately, and not particularly welcoming.\n"]

        intro = hallwayIntros[random.randint(0,len(hallwayIntros)-1)]
        print(textwrap.fill(intro, 60))

        nextRoom = Engine()
        nextRoom.pickRoom()

class Lounge(Room):
    pass

class DiningRoom(Room):
    pass

class Engine(object):

    def pickRoom(self):
        #dictionary with the calls we'll need to move to a new room
        roomsDictionary = {'Kitchen': Kitchen(playerCards, NPCCards),
                           'Ballroom': Ballroom(playerCards, NPCCards),
                           'Conservatory': Conservatory(playerCards, NPCCards),
                           'Dining Room': DiningRoom(playerCards, NPCCards),
                           'Cellar': Cellar(playerCards, NPCCards),
                           'Billiard Room': BilliardRoom(playerCards, NPCCards),
                           'Library': Library(playerCards, NPCCards),
                           'Study': Study(playerCards, NPCCards),
                           'Lounge': Lounge(playerCards, NPCCards)}

        #converting the dictionary to a list
        roomsList = []

        for keys in roomsDictionary.keys():
            roomsList.append(keys)

        #get the user's room choice
        roomChoice = input("\n> Where do you want to go? Choose from from one of the below:\n" + str(CluedoRooms.rooms) + "\n> ")

        #Make sure the user's room choice is in the rooms list
        while roomChoice not in roomsList:
            roomChoice = input("\n> That doesn't look right. Choose from from one of the below:\n" + str(CluedoRooms.rooms) + "\n> ")
        else:
            nextRoom = roomsDictionary.get(roomChoice)

            #move to the next room
            nextRoom.enter()

    def makeAGuess(self, playerCards, NPCCards):
        #pass the dealt cards through
        self.playerCards = playerCards
        self.NPCCards = NPCCards

        # check the NPCCards are carried through properly
        #print(NPCCards)

        murdererGuess = input("> Who do you think did it?\n" + "Choose from one of the following: \n" + str(CluedoCharacters.characters) + "\n> ")

        if murdererGuess in CluedoCharacters.characters:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options:")
            print(f"{CluedoCharacters.characters}")
            murdererGuess = input("> Out of these folks, who do you think did it? ")

        weaponGuess = input("> Which weapon do you think they used?\n" + "Choose from one of the following: \n" + str(CluedoWeapons.weapons) + "\n> ")

        if weaponGuess in CluedoWeapons.weapons:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options: ")
            print(f"{CluedoWeapons.weapons}")
            weaponGuess = input("> Out of these folks, which do you think is the weapon? ")

        roomGuess = input("> And where do you think they did it?\n" + "Choose from one of the following: \n" + str(CluedoRooms.rooms) + "\n> ")

        if roomGuess in CluedoRooms.rooms:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options: ")
            print(f"{CluedoRooms.rooms}")
            roomGuess = input("> Where do you think the murder happened? ")

        print(f"So you think {murdererGuess} did it, with the {weaponGuess} in the {roomGuess}. Let's see!")

        #create a list with the user's guess
        guess = []
        guess.append(murdererGuess)
        guess.append(weaponGuess)
        guess.append(roomGuess)

        #check the list creation for the guess is working correctly
        #print(guess)

        #create another list to hold matches from the user's guesses
        i = 0
        matches = []

        #run through the user's guess, add any matches to the list we just created
        while i < len(guess):
            if guess[i] in NPCCards:
                print(guess[i])
                matches.append(guess[i])
                i = i + 1
            else:
                i = i + 1
        else:
            print(f"Your opponents have the following cards:\n{matches}")

    def accuse(self, murdererGuess, roomGuess, weaponGuess):
        self.murdererGuess = murdererGuess
        self.roomGuess = roomGuess
        self.weaponGuess = weaponGuess

        print(f"{murdererGuess}, {roomGuess}, {weaponGuess}")

class setUpGame(object):

    def setUpMurder(self):
        murdering = "Murdering..."

        for i in range(len(murdering)):
            print(murdering[i], end='', flush=True);
            time.sleep(0.2)

        # Assign a random murderer from the available characters
        murderer = CluedoCards.characters[random.randint(0,len(CluedoCards.characters)-1)]
        print(f"\n{murderer}")
        # Remove the murderer from the deck
        CluedoCards.characters.remove(str(murderer))
#        print(f"{CluedoCards.characters}")

        # Assign a random weapon from the available weapons
        weapon = CluedoCards.weapons[random.randint(0,len(CluedoCards.weapons)-1)]
        print(f"{weapon}")
        # Remove the weapon from the deck
        CluedoCards.weapons.remove(str(weapon))
#        print(f"{CluedoCards.weapons}")

        # Assign a random room from the available rooms
        room = CluedoCards.rooms[random.randint(0,len(CluedoCards.rooms)-1)]
        print(f"{room}")
        # Remove the weapon from the deck
        CluedoCards.rooms.remove(str(room))
#        print(f"{CluedoCards.rooms}")
        print("...Done.")

        return murderer, weapon, room

    def dealCards(self):
        playerCards = []
        NPCCards = []

        numPlayers = range(int(input("> How many players do you want to play against? ")))

        i = 0

        while len(CluedoCards.characters) > i:
            playerCards.append(CluedoCards.characters.pop())
            for i in numPlayers:
                NPCCards.append(CluedoCards.characters.pop()) if CluedoCards.characters else None

        while len(CluedoCards.weapons) > i:
            playerCards.append(CluedoCards.weapons.pop())
            for i in numPlayers:
                NPCCards.append(CluedoCards.weapons.pop()) if CluedoCards.weapons else None

        while len(CluedoCards.rooms) > i:
            playerCards.append(CluedoCards.rooms.pop())
            for i in numPlayers:
                NPCCards.append(CluedoCards.rooms.pop()) if CluedoCards.rooms else None

        #check the lists for cards being dealt work correctly
        #print(f"{playerCards}")
        #print(f"{NPCCards}")

        print("Lovely!")
        progress = input("> Ready to start? Type Y or N\n")

        if progress == "Y":
            print(f"\n.....................................\n")
            return playerCards, NPCCards
        elif progress == "N":
            print(f"Guess the murder isn't getting solved then! Nice knowing you!")
            exit(1)
        else:
            print(f"That doesn't look quite right.")
            progress = input("> Type Y or N\n")

            if progress == "Y":
                print(f"\n.....................................\n")
                return playerCards, NPCCards
            else:
                print(f"Guess the murder isn't getting solved then! Nice knowing you!")
                exit(1)

#print(f"Glad you could join us, but terribly sorry it had to be under these circumstances)

setUp = setUpGame()
murder = setUp.setUpMurder()

#Return the murder cards
murder = list(murder)
#print(murder)

#convert the murder tuple to a list
murder = list(murder)

#Get the murderer, weapon and room
murderer = murder[0]
weapon = murder[1]
room = murder[2]

#Deal the cards, return the cards held by players as two lists - PlayerCards & NPCCards
cards = setUp.dealCards()

#Get the player's cards
playerCards = list(cards[0])

#Get the NPC's cards
NPCCards = list(cards[1])

#opening scene for the game
sceneSetting = []
sceneSetting = ["There's a dense fog in the air as you approach the manor. Nightmare Inn, you think he called it on the phone. Accurate.",
                "Gates of rusted iron burst open, and so you begin the approach towards the door. Knotted branches of trees line the drive on the way up, illuminated by occasional flashes of lightning.",
                "Looking over to the manor, you can see what looks like the remnants of a dinner party. A silent, rather unlively one at that."]

#print the sceneSetting variable from a list, as the textwrap function below doesn't enforce \n for new lines. Each item in the list prints on a new line instead.
for i in range(len(sceneSetting)):
    print(textwrap.fill(sceneSetting[i], 60))

knock = input("\n> Are you ready to knock on the door? Y/N\n")

#options for story progression
if knock == "Y":
    firstScene = Lobby(playerCards, NPCCards)
    firstScene.enter()
elif knock == "N":
    print(f"Well... I guess this murder will go unsolved then. Some investigator you are.")
else:
    print(f"That doesn't look quite right. Type Y or N.")
    knock = input("> Are you ready to knock on the door? Type Y or N\n")
    if knock == "Y":
        firstScene = Lobby(playerCards, NPCCards)
        firstScene.enter()
    else:
        print(f"Well... I guess this murder will go unsolved then. Some investigator you are.")

#start = Engine()
#start.makeAGuess(playerCards, NPCCards)
#nextRoom = start.pickRoom()
