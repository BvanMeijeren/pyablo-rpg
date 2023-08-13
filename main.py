from graphics import *
from encounters import *
from level_up import *
from lootgenerator import *
import os

def game_engine(mainchar, weapon):
    # Intro text
    print_slow('You wake up in the forest, without a memory of how you got there.')
    print_slow('You feel like you are level 1 in a text-based RPG and have the sudden urge to kill monsters and collect shiny things.')
    print_slow('Press enter to start your journey.')
    userinput = 'y'

    while userinput != 'q':
        userinput = input('> ')

        # Create encounter
        encounter(mainchar, weapon, userinput)

        # Loot
        generate_loot(mainchar)

        # Check if level up
        level_up(mainchar)
        

    print_slow('Exiting game...')
    print_slow('Bye!')

