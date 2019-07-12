from room import Room
from player import Player
from start import newCharacter
from enemy import Enemy
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Enemy("Ghoul")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Enemy("Werewolf")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", None),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Enemy("Vampire")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

 


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
    if player.hasTreasure == False:
        player.next()
    else:
        print(f"\nYou've found the treasure and defeated all of the monsters that terrorize these lands. Your adventuresome soul would wither if you stayed. Alas, the time has come for you to part ways with this place and travel onward to new lands, with new adventures. Farewell, {player.name}. Tales of your heroism will forever be told in this place.")
        action = "Q"

    

