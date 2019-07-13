from room import Room
from player import Player
from start import newCharacter
from enemy import Enemy
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. \nDusty
passages run north and east.""", Enemy("Ghoul"), ["bag of grain","doll"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. \nAhead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Enemy("Werewolf"), ["moon powder"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Enemy("White Walker"), ["antidote", "Valerian Steel Shield"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! What could be in here?""", Enemy("Vampire"), ["Treasure"]),

'library':   Room("Grand Library", """You walk through a pair of heavy victorian doors into a grand circular room with walls that are lined with shelves of dusty tombs. \nThe only light comes from the moonlight that pours in from the dusty windows across the room.  \nIn the center of room hangs a grand chandelier that, many years ago, must have shone marvelously in moonlight. \nYears of neglect have robbed the room of its splendor.""", Enemy("Siren of the Night"), ["spellbook", "candles"])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['overlook']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['library'].e_to = room['foyer']
room['foyer'].w_to = room['library']

 


## Begin New Game
player = newCharacter(room["outside"])
action = ""



while action != "Q":
    if player.hp < 0:
        time.sleep(1)
        print(f'\nSorry, but you are not cut out for this land. Goodbye, {player.name}.')
        action = "Q"
    time.sleep(2)
    print(f'\n\nWelcome to the Land of Id, {player.name}. Adventure awaits. Lets begin.\n')
    player.locate()
    player.move()
    while player.hasTreasure == False:
        player.next()
    if player.hasTreasure == True:
        time.sleep(1)
        print("\n!!!\n")
        time.sleep(1)
        print(f"\nYou've found the treasure and defeated all of the monsters that terrorize these lands.\n")
        time.sleep(1)
        print("\nYour adventuresome soul would wither if you stayed. Alas, the time has come for you to part ways with this place and travel onward to new lands, with new adventures.\n") 
        time.sleep(1) 
        print(f"Farewell, {player.name}. Tales of your heroism will forever be told in this place.\n\n")
        action = "Q"

    

