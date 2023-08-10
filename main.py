from execute_subprocess import execute_python_file
from characters import Character
from weapons import *
from character_creation import *
from enemies import enemies
from encounter import *
import os

def game_engine(mainchar, weapon):
    # Intro text
    print('You wake up in the forest, without a memory of how you got there.')
    print('You feel like you are level 1 in a text-based RPG and have the sudden urge to kill monsters and collect shiny things.')
    print('Pess enter to continue')
    userinput = 'y'

    while userinput != 'q':
        userinput = input()
        encounter(mainchar, weapon, userinput)
        

    print('Exiting game...')
    print('Bye!')

