from execute_subprocess import execute_python_file
from character_creation import *
from main import *

# Intro text
print("Welcome to Pyablo, my tryout text-based RPG!")
print("You will now enter the lands to goblins, skeletons and heroes. Prepare to loot!")

# Main menu
print('What would you like to do? Press s to start a new game or q to close the program.')
x = input('> ')

if x == 's':
    print('Starting a new game...')
    # Character creation menu
    mainchar = character_creation()

    # Create starterweapon for mainchar
    starterweapon = create_starterweapon()

    # Start up the game engine (main) with encounters
    game_engine(mainchar, starterweapon)
else:
    print('Bye!')

