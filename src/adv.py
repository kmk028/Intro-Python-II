from room import Room
from player import Player
from item import Item
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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#list of items

items = {'greatsword': Item("greatsword","Ancient sword of Elves"),
        'warhammer': Item("warhammer","Dwarven WarHammer"),
        'Armor': Item("Armor","Dragonscale armor"),
        'Potion': Item("Potion","Potion of resist Poison"),
        'Banner': Item("Banner","House Banner"),
        'Ring': Item("Ring","Pearl Ring")}

#Put items in Rooms

room['foyer'].items = [items['greatsword'],items['Potion']]
room['treasure'].items = [items['Ring']]
room['overlook'].items = [items['Banner']]
room['narrow'].items = [items['Armor'],]

print (room['foyer'].items)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input ('State thy name adventurer! : ')
player = Player(name,room['outside'])

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

# Create a dict of possible directions
directions = {'N':'n_to', 'S':'s_to', 'E':'e_to', 'W':'w_to'}
#Print the current position of player. 
print(f"###### {player.name}, you are at {player.current_room.name}######")

while True:
    
    choice = input('Where do you want to go? (Press N for North, E for east , W for West , S for South. Q for quit game')
    # if user choice is valid move player to new location and print it, 
    # if Choice is to quit then break out of loop
    # if choice is invalid then ask for valid input. 
    if choice in directions.keys():
        direction = directions[choice]
        previous_room = player.current_room
        try:
            player.current_room  = getattr(player.current_room,direction)
            print(f"###### {player.name}, you are at {player.current_room.name}######")
        except AttributeError:
            player.current_room = previous_room
            print('Cannot go that way! Choose again. ')
    elif choice is 'Q':
        print ('Good bye adventurer! Thanks for Playing :)')
        break
    else:
        print('Invalid choice! Choose again.')
