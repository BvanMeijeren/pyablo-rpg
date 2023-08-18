from character_creation import *
from graphics import *
from main import *
import os

def start_game():
    # Intro text
    print_slow("Welcome to Pyablo!")
    print_slow("You will now enter the lands to goblins, skeletons and heroes. Prepare to loot!")

    # Main menu
    print_slow('What would you like to do? Press s to start a new game or q to close the program.')
    x = input('> ')

    if x == 's':
        print_slow('Starting a new game...')
        time.sleep(1.0)
        os.system('cls')
        # Character creation menu
        mainchar = character_creation()
        time.sleep(1.0)
        os.system('cls')

        # Create starterweapon for mainchar
        starterweapon = create_starterweapon()
        mainchar.equipped_weapon = starterweapon # equip weapon

        # Start up the game engine (main) with encounters
        game_engine(mainchar, starterweapon)

    else:
        print_slow('Bye!')

start_game()

