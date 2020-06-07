from room import Room
from player import Player
# Declare all the rooms
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


# Main

# Make a new player object that is currently in the 'outside' room.
print("""

                               <<< Welcome To The Game >>>

""")
name = input("""

What's your name, Young Man? """)
player = Player(name, room['outside'])

print(
    f"""  
    
                                                  welcome {player.name}


Your Journey start from room:
{player.current_room}


                        [W]for North 👆   [S] for South 👇  [D] for East 👉 [A] for West 👈 [Q] to Quit 🙁

 """)


while True:
    user_direction = input("Next move ?  ").upper()
    if user_direction == 'W':
        next_move = player.current_room.n_to
        if next_move == None:
            print("Blocked, Try picking a new direction.")
        else:
            player = Player(name, next_move)
            print(player.current_room)
    elif user_direction == 'S':
        next_move = player.current_room.s_to
        if next_move == None:
            print("Blocked, Try picking a new direction.")
        else:
            player = Player(name, next_move)
            print(player.current_room)

    elif user_direction == 'D':
        next_move = player.current_room.e_to
        if next_move == None:
            print("Blocked, Try picking a new direction.")
        else:
            player = Player(name, next_move)
            print(player.current_room)

    elif user_direction == 'A':
        next_move = player.current_room.w_to
        if next_move == None:
            print("Blocked, Try picking a new direction.")
        else:
            player = Player(name, next_move)
            print(player.current_room)

    elif user_direction == 'Q':
        print(f"Thanks for playing {name}! Come back soon!")
        break
