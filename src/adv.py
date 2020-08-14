from room import Room
from player import Player
from item import Items
import textwrap
# Declare all the rooms

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

# Declare Items
items = {
    'key': Items("Key", """An old, rustic looking key probably unlocks something ancient."""),
    'candle': Items("Candle", """A standard wax candle used to light the room""")
}


# Link rooms together

room['outside'].connection["n"] = room['foyer']
room['foyer'].connection["s"] = room['outside']
room['foyer'].connection["n"] = room['overlook']
room['foyer'].connection["e"] = room['narrow']
room['overlook'].connection["s"] = room['foyer']
room['narrow'].connection["w"] = room['foyer']
room['narrow'].connection["n"] = room['treasure']
room['treasure'].connection["s"] = room['narrow']

# Link items to rooms
room['overlook'].addItem(items['key'])
room['narrow'].addItem(items['candle'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("kennith", room['outside'])
for line in textwrap.wrap(player.current_room.description, 20):
    print(line)
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

user_is_playing = True

while user_is_playing:

    user_input = input(
        "Which direction would you like to go? (n/e/s/w)----").lower()

    if user_input in ["n", "e", "s", "w"]:
        player.move(user_input)
        print('You are currently---', player.current_room.name)
        for line in textwrap.wrap(player.current_room.description, 40):
            print(line)
    elif user_input == "q":
        print("You exited the game. Thanks for playing!")
        user_is_playing = False
# TODO:
    if len(player.current_room.loot) > 0:
        print("'Items in the room' =", player.current_room.loot[0].name)
        user_input = input(
            "would you like to pick up the item? get (item name)/no----").lower()

    if len(user_input.split()) == 2:

        get_handle = user_input.split()

        if get_handle[0] == "get":
            target_item = get_handle[1]
            for i in player.current_room.loot:
                player.pickUpItem(i)
                player.current_room.removeItem(i)
                print("You picked up:", i.name)
            for i in player.inventory:
                print("Player Inventory:", i.name)

        else:
            get_handle[0] == "drop"
            target_item = get_handle[1]
            for i in player.inventory:
                if i == target_item:
                    player.dropItem(i)
                    player.current_room.addItem(i)
                    print(
                        i, "removed from inventory and added to the room\n Player inventory", player.inventory)
