from graphics import *
from encounters import *
from level_up import *
from lootgenerator import *
from mapgenerator import *
from map_navigator import *
import os

def game_engine(mainchar, weapon):
    # Intro text
    print_slow('You wake up in the forest, without a memory of how you got there.')
    print_slow('You feel like you are level 1 in a text-based RPG and have the sudden urge to kill monsters and collect shiny things.')
    print_slow('Press enter to start your journey.')
    time.sleep(1.0)


    userinput = 'y'
    you_are_dead = False
    trail = {0:2} # choices made by player in the current map
    map_structure = []

    while userinput != 'q':
        userinput = input('> ')

        # generate a map
        if trail == {0:2}: # if trail is only empty, generate new map
            print('Generating new map...')
            map_structure = generate_map_structure(mainchar) 
            visualize_vertical_map(map_structure, trail)
            print('You set out to traverse the lands laid out before you...')
        else: # else continue on current one
            navigate_map(map_structure, trail)
            # choose where to go
            


        # Create encounter, check if player is still alive
        os.system('cls')
        you_are_dead = encounter(mainchar, weapon, userinput)

        if you_are_dead == False:
            # Loot
            generate_loot(mainchar)

            # Check if level up
            level_up(mainchar)
        else:
            userinput = 'q'
        

    print_slow('Exiting game...')
    print_slow('Bye!')

