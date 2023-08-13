from execute_subprocess import execute_python_file
from encounters import *
from level_up import *
from lootgenerator import *
import os

def game_engine(mainchar, weapon):
    # Intro text
    print('You wake up in the forest, without a memory of how you got there.')
    print('You feel like you are level 1 in a text-based RPG and have the sudden urge to kill monsters and collect shiny things.')
    print('Press enter to start your journey.')
    userinput = 'y'

    while userinput != 'q':
        userinput = input('> ')

        # Create encounter
        encounter(mainchar, weapon, userinput)

        # Loot
        generate_loot(mainchar)

        # Check if level up
        level_up(mainchar)
        

    print('Exiting game...')
    print('Bye!')

