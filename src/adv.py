from room import Room
from player import Player

# Declare all the rooms

#this is a dictionary
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
import sys

player = Player('Bob', room['outside'])

move = 0

while move != len(sys.argv) + 1:

    move = input("Please make a move: \n")
    
    move = str(move)


    if move == "n":
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
            
            print(f"room: {player.current_room.name}\t description: {player.current_room.description}\n")
        else:
            print("Whoops, there's no room there!")
    elif move == "s":
       
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to

            print(f"room: {player.current_room.name}\t description: {player.current_room.description}")
        else:
            print("Whoops, there's no room there!")
    elif move == "e":
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to

            print(f"room: {player.current_room.name}\t description: {player.current_room.description}")
        else:
            print("Whoops, there's no room there!")
    elif move == "w":
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
            
            print(f"room: {player.current_room.name}\t description: {player.current_room.description}")
        else:
            print("Whoops, there's no room there!")
    elif move == "q":
        print("You have exited the game")
        break
    else:
        print("Please input a cardinal direction: n, s, e, or w")
        