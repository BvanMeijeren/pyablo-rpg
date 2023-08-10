from main import *
from enemies import enemies
from character_creation import *
import random 
import os

enemy = random.choice(enemies)

def encounter(mainchar, weapon, userinput):
    # encounter intro + options
    print('A wild ' + enemy.name + ' has appeared! What will you do?')
    print('Press a to attack the ' + enemy.name, 
        'Press h to use a healing potion',
        sep=os.linesep)

    # Player's turn
    if userinput == 'a':
        damage = weapon.damage
        enemy.hitpoints = enemy.hitpoints - damage 
        print('You hit the ' + enemy.name + ' for ' + str(damage) + '! It has ' + str(enemy.hitpoints) + ' left.')
    elif userinput == 'h':
        mainchar.hitpoints + 25

    # Enemy's turn
    mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damge
    print(enemy.name + ' hit you for ' + str(enemy.enemy_damge) + ' damage. ' + str(mainchar.hitpoints) + '/100 HP remaining.')