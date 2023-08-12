from enemies import enemies
from enemy_actions import *
import random 
import os
from player_actions import *

# encounter function
def encounter(mainchar, weapon, userinput):

    # determine enemy and set encounter game state
    enemy = random.choice(enemies)(mainchar, weapon)
    encounter_ended = False

    # encounter intro + options
    print('A ' + enemy.name + ' has appeared!')
    print(enemy.name + ' will use ' + '. What will you do?')
    print(keybindings)
    
    # encounter instance
    while encounter_ended == False and userinput != 'q':
        userinput = input('> ')

        # Determine enemy action
        enemy_action = random.choice(enemy_actions)
        print(enemy.name + ' will use ' + enemy_action + '.')

        # Player's turn
        if userinput != 'q':
            exec(keybindings[userinput]+'(mainchar, enemy, weapon)') # execute selected player action
        else:
            encounter_ended = True
        # Check if enemy died
        if enemy.hitpoints <= 0:
            print(enemy.name + ' was slain, which increased your XP by '+ str(enemy.xp) + '! You venture on...')
            encounter_ended = True
            mainchar.xp = mainchar.xp + enemy.xp

        # Enemy's turn
        if encounter_ended == False:
            mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damge
            print(enemy.name + ' hit you for ' + str(round(enemy.enemy_damge)) + ' damage. ' + 
                  str(round(mainchar.hitpoints)) + ' HP remaining.')

