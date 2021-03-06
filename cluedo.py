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

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "You wouldn't know there'd been a dinner party this evening, if you looked at the Kitchen at least. There's plenty of potentially suspicious items in this room though, so you get to work. "

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        roomName = 'Kitchen'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class Ballroom(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "The ballroom's dank and clearly hasn't been given any attention in decades. You can't see any open windows, but a musty chandelier jangles as the breeze from outside finds its way in. There's a dust coated Baby Grand in the corner, and you just can't help yourself..."

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        numPlinks = 3
        start = 0

        print("\n")

        while start < numPlinks:
            print(f"*PLINK*")
            time.sleep(1)
            start += 1

        time.sleep(2)

        print(f"\nBut you didn't come here to play piano, you came to solve a murder.\n")

        time.sleep(2)

        roomName = 'Ballroom'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class Conservatory(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "Rain rattles the window panes throughout the Conservatory. What's usually a gentle, reassuring sound is broken by the occasional crack of thunder, and the shadows from lightning thrown across the room."

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        roomName = 'Conservatory'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class Cellar(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "You open the cellar door and head down. Though underground there's no escape from the slapping of rain outside, just now with added damp."

        print(textwrap.fill(sceneSetting, 60))

        accusationIntro = "You spend some time putting the final pieces of the puzzle together, and you're ready to go."

        return None

class BilliardRoom(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "The Billiard Room is vast, with swathes of space largely unused - just a bar and a pool table right there in the center. Of course, you can't help yourself but take a cue...\n"

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        print(f"\n*THUNK*")

        time.sleep(2)

        print(f"\nStraight in the pocket.")

        time.sleep(2)

        print(f"\nLet's hope this case proves just as easy\n")

        time.sleep(2)

        roomName = 'Billiard Room'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class Library(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "Mr. Body clearly had a lot of time on his hands, was extremely well read, or at the very least he wanted to look like he was. From floor to ceiling, books line the walls. The smell of mahogany and leather bound books fill the air, and the golden spines of books glisten from nearby candlelight."

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        roomName = 'Library'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class Study(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "The study must have some of Mr. Body's personal items, any of which could lead you to the murder. Time to dig deep."

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        roomName = 'Study'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class Lobby(Room):

    def enter(self):
        #enter the lobby, start the door knock as part of story progression
        print(f"\n.....................................")
        #knock = 'KNOCK'
        numKnocks = 3
        start = 0

        print("\n")

        while start < numKnocks:
            print(f"*KNOCK*")
            time.sleep(1)
            start += 1

        time.sleep(1)

        print(f"\nThere's a faint sound of footsteps approaching...\n")

        time.sleep(3)

        butlerIntro = "The person who greets you has seen better days. Aghast, dishevelled, and clearly beside himself."
        print(textwrap.fill(butlerIntro, 60))

        time.sleep(5)

        print(f"\nBUTLER:")

        butlerDialogue = """Oh my - thank God you've arrived! I'm Jeeves, the butler at this fine establishment. There's been a terrible accident. You see, one of our guests... Mr. Body. He's been murdered! It's positively ghastly!\n"""

        print(textwrap.fill(butlerDialogue, 60, initial_indent='       ', subsequent_indent='      '))

        time.sleep(5)

        print("\n")
        playerCardsIntro = "You continue chatting with the butler for a while. He's withdrawn, and probably in shock, but it's a productive chat. Now you can rule out the following with some certainty:"
        print(textwrap.fill(playerCardsIntro, 60))
        print(f"\n{playerCards}")

        print(f"\nThese are your cards. Make a note of them :)")

        time.sleep(5)

        progress = input("\n> Are you ready to start investigating? Y/N\n").upper()

        #options based on user input
        if progress == "Y":
            nextScene = Hallway(playerCards, NPCCards)
            nextScene.enter()
        elif progress == "N":
            #call the list of early finish options, declared at the start of the code
            quip = earlyFinishes()
            quip = quip.earlyFinishes[random.randint(0,len(quip.earlyFinishes)-1)]
            print(f"{quip}")
        else:
            print("That doesn't look quite right. Type Y or N")
            progress = input("> Are you ready to start investigating? Y/N\n").upper()
            if progress == "Y":
                nextScene = Hallway(playerCards, NPCCards)
                nextScene.enter()
            else:
                quip = earlyFinishes()
                quip = quip.earlyFinishes[random.randint(0,len(quip.earlyFinishes)-1)]
                print(f"{quip}")

class Hallway(Room):

    def enter(self):
        print(f"\n.....................................\n")

        hallwayIntros = ["The hallways are eerily silent, aside from the faint whispers of the guests. You tune them out for now, and you're pushing on.",
                         "You head over to the hallway. The whole place has a stately air, but it's not welcoming in any way, shape or form. You'll be glad to leave this place soon."]

        intro = hallwayIntros[random.randint(0,len(hallwayIntros)-1)]
        print(textwrap.fill(intro, 60))

        nextRoom = Engine()
        nextRoom.pickRoom()

class Lounge(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "As you approch the Lounge, there's a chorus of 'Shake, Rattle and Roll' ringing out from the record player. Just outside the door, you hear faint whispers from the night's suspects - this is where they're keeping themselves for the night. There's silence the second you walk in, and they watch you like a hawk as you look around."

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        roomName = 'Lounge'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

class DiningRoom(Room):

    def enter(self):
        print(f"\n.....................................\n")

        sceneSetting = "The smell from the Dining Room is glorious. The murder happened early in the evening, as not a single meal is finished. Candles lined along the dining table light the room, and you take a look around."

        print(textwrap.fill(sceneSetting, 60))

        time.sleep(5)

        roomName = 'Dining Room'

        guess = Engine()
        guess.makeAGuess(playerCards, NPCCards, roomName)
        guess.pickRoom()

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

        print(f"\n.....................................\n")

        #get the user's room choice
        roomChoice = input("\n> Where do you want to go? Choose from from one of the below:\n" + str(CluedoRooms.rooms) + "\n> ")

        #Make sure the user's room choice is in the rooms list
        while roomChoice not in roomsList:
            roomChoice = input("\n> That doesn't look right. Choose from from one of the below:\n" + str(CluedoRooms.rooms) + "\n> ")
        else:
            nextRoom = roomsDictionary.get(roomChoice)

            #move to the next room
            nextRoom.enter()

    def makeAGuess(self, playerCards, NPCCards, roomName):
        print(f"\n.....................................\n")
        print(f"\nIt's time to make a guess.\n")
        #pass the dealt cards through
        self.playerCards = playerCards
        self.NPCCards = NPCCards
        self.roomName = roomName

        # check the NPCCards are carried through properly
        #print(NPCCards)

        murdererGuess = input("\n> Who do you think did it?\n" + "Choose from one of the following: \n" + str(CluedoCharacters.characters) + "\n> ")

        if murdererGuess in CluedoCharacters.characters:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options:")
            print(f"{CluedoCharacters.characters}")
            murdererGuess = input("> Out of these folks, who do you think did it? ")

        weaponGuess = input("\n> Which weapon do you think they used?\n" + "Choose from one of the following: \n" + str(CluedoWeapons.weapons) + "\n> ")

        if weaponGuess in CluedoWeapons.weapons:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options: ")
            print(f"{CluedoWeapons.weapons}")
            weaponGuess = input("> Out of these folks, which do you think is the weapon? ")

#        roomGuess = input("> And where do you think they did it?\n" + "Choose from one of the following: \n" + str(CluedoRooms.rooms) + "\n> ")
#
#        if roomGuess in CluedoRooms.rooms:
#            pass
#        else:
#            print(f"That doesn't look quite right. Rememember, these are the options: ")
#            print(f"{CluedoRooms.rooms}")
#            roomGuess = input("> Where do you think the murder happened? ")

        print(f"\n.....................................\n")
        print(f"\nSo you think {murdererGuess} did it, with the {weaponGuess} in the {roomName}. Let's see!")

        time.sleep(5)

        #create a list with the user's guess
        guess = []
        guess.append(murdererGuess)
        guess.append(weaponGuess)
        guess.append(roomName)

        #check the list creation for the guess is working correctly
        #print(guess)

        #create another list to hold matches from the user's guesses
        i = 0
        matches = []

        #run through the user's guess, add any matches to the list we just created
        while i < len(guess):
            if guess[i] in NPCCards:
                matches.append(guess[i])
                i = i + 1
            else:
                i = i + 1
        else:
            print(f"\nYour opponents have the following cards:\n{matches}")

    def accuse(self, murderer, room, weapon):
        self.murderer = murderer
        self.room = room
        self.weapon = weapon

        murder = []
        murder.append(murderer)
        murder.append(weapon)
        murder.append(room)

        print(f"\n.....................................\n")
        print(f"\nOkay, it's time to make your accusation\n")

        murdererAccusation = input("\n> Who do you think did it?\n" + "Choose from one of the following: \n" + str(CluedoCharacters.characters) + "\n> ")

        if murdererAccusation in CluedoCharacters.characters:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options:")
            print(f"{CluedoCharacters.characters}")
            murdererAccusation = input("> Out of these folks, who do you think did it? ")

        weaponAccusation = input("\n> Which weapon do you think they used?\n" + "Choose from one of the following: \n" + str(CluedoWeapons.weapons) + "\n> ")

        if weaponAccusation in CluedoWeapons.weapons:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options: ")
            print(f"{CluedoWeapons.weapons}")
            weaponAccusation = input("> Out of these folks, which do you think is the weapon? ")

        roomAccusation = input("\n> And where do you think they did it?\n" + "Choose from one of the following: \n" + str(CluedoRooms.rooms) + "\n> ")

        if roomAccusation in CluedoRooms.rooms:
            pass
        else:
            print(f"That doesn't look quite right. Rememember, these are the options: ")
            print(f"{CluedoRooms.rooms}")
            roomAccusation = input("> Where do you think the murder happened? ")

        print(f"\nSo you think {murdererAccusation} did it, with the {weaponAccusation} in the {roomAccusation}. Let's see!")

        #create a list with the user's guess
        accusation = []
        accusation.append(murdererAccusation)
        accusation.append(weaponAccusation)
        accusation.append(roomAccusation)

        #check the list creation for the guess is working correctly
        #print(accusation)

        #create another list to hold matches from the user's guesses
        i = 0
        matches = []

        #run through the user's guess, add any matches to the list we just created
        while i < len(accusation):
            if accusation[i] in murder:
                matches.append(accusation[i])
                i = i + 1
            else:
                i = i + 1
        else:
            None

        if murder == accusation:
            print(f"\n{murderer} crumbles before your very eyes!")
            time.sleep(3)
            print(f"Here's how it played out: \n{matches}")
        else:
            print(f"Sadly you were off the mark this time.")
            time.sleep(2)
            print(f"Here's how it went down: \n{murder}")

        return None

class setUpGame(object):

    def setUpMurder(self):
        murdering = "Murdering..."

        for i in range(len(murdering)):
            print(murdering[i], end='', flush=True);
            time.sleep(0.2)

        # Assign a random murderer from the available characters
        murderer = CluedoCards.characters[random.randint(0,len(CluedoCards.characters)-1)]
#        print(f"\n{murderer}")
        # Remove the murderer from the deck
        CluedoCards.characters.remove(str(murderer))
#        print(f"{CluedoCards.characters}")

        # Assign a random weapon from the available weapons
        weapon = CluedoCards.weapons[random.randint(0,len(CluedoCards.weapons)-1)]
#        print(f"{weapon}")
        # Remove the weapon from the deck
        CluedoCards.weapons.remove(str(weapon))
#        print(f"{CluedoCards.weapons}")

        # Assign a random room from the available rooms
        room = CluedoCards.rooms[random.randint(0,len(CluedoCards.rooms)-1)]
#        print(f"{room}")
        # Remove the weapon from the deck
        CluedoCards.rooms.remove(str(room))
#        print(f"{CluedoCards.rooms}")
        print("\nDone.")

        return murderer, weapon, room

    def dealCards(self):
        playerCards = []
        NPCCards = []

        #ask user for number of players, the number will be used to share out the cards to this number + 1 more (the player)
        numPlayers = input("\n> How many players do you want to play against? ")

        try:
            numPlayers = int(numPlayers)
        except ValueError:
            print(f"That's not an integer! Try again.")
            numPlayers = input("\n> How many players do you want to play against? ")
            try:
                numPlayers = int(numPlayers)
            except ValueError:
                print(f"Well, guess you won't be solving any crimes today.")
                exit(1)

        i = 0

        numPlayersRange = range(int(numPlayers))

        #take a card out of the deck for the player, then take x number of cards out of the deck based on how users you wnated to play against
        while len(CluedoCards.characters) > i:
            playerCards.append(CluedoCards.characters.pop())
            for i in numPlayersRange:
                NPCCards.append(CluedoCards.characters.pop()) if CluedoCards.characters else None

        while len(CluedoCards.weapons) > i:
            playerCards.append(CluedoCards.weapons.pop())
            for i in numPlayersRange:
                NPCCards.append(CluedoCards.weapons.pop()) if CluedoCards.weapons else None

        while len(CluedoCards.rooms) > i:
            playerCards.append(CluedoCards.rooms.pop())
            for i in numPlayersRange:
                NPCCards.append(CluedoCards.rooms.pop()) if CluedoCards.rooms else None

        print("Lovely!")

        #Find out if the user wants to start, and some validation handling
        progress = input("\n> Ready to start? Type Y or N\n").upper()

        if progress == "Y":
            print(f"\n.....................................\n")
            return playerCards, NPCCards
        elif progress == "N":
            print(f"Guess the murder isn't getting solved then! Nice knowing you!")
            exit(1)
        else:
            print(f"That doesn't look quite right.")
            progress = input("> Type Y or N\n").upper()

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

knock = input("\n> Are you ready to knock on the door? Y/N\n").upper()

#options for story progression
if knock == "Y":
    firstScene = Lobby(playerCards, NPCCards)
    firstScene.enter()
elif knock == "N":
    print(f"Well... I guess this murder will go unsolved then. Some investigator you are.")
else:
    print(f"That doesn't look quite right. Type Y or N.")
    knock = input("> Are you ready to knock on the door? Type Y or N\n").upper()
    if knock == "Y":
        firstScene = Lobby(playerCards, NPCCards)
        firstScene.enter()
    else:
        print(f"Well... I guess this murder will go unsolved then. Some investigator you are.")
        exit(1)

accusation = Engine()
accusation.accuse(murderer, room, weapon)

exit(1)
