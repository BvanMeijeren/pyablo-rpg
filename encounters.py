from enemies import enemies
import random 
import os
from playeractions import *

# encounter function
def encounter(mainchar, weapon, userinput):

    # determine enemy and set encounter game state
    enemy = random.choice(enemies)
    encounter_ended = False

    # encounter intro + options
    print('A ' + enemy.name + ' has appeared!')
    print(enemy.name + ' will use ' + '. What will you do?')
    print(keybindings)
    
    # encounter instance
    while encounter_ended == False:
        userinput = input('> ')
        # Player's turn
        exec(keybindings[userinput]+'(mainchar, enemy, weapon)') # execute selected action
        # Check if enemy died
        if enemy.hitpoints <= 0:
            print(enemy.name + ' was slain! You venture on...')
            encounter_ended = True

        # Enemy's turn
        if encounter_ended == False:
            mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damge
            print(enemy.name + ' hit you for ' + str(enemy.enemy_damge) + ' damage. ' + str(mainchar.hitpoints) + '/' +
                  enemy.hitpoints + '100 HP remaining.')


# def encounter(mainchar, weapon, userinput):

#     # determine enemy and set encounter game state
#     enemy = random.choice(enemies)
#     encounter_ended = False

#     # encounter intro + options
#     print('A ' + enemy.name + ' has appeared! What will you do?')
#     print('Press a to attack the ' + enemy.name, 
#         'Press h to use a healing potion',
#         sep=os.linesep)
    
#     # encounter
#     while encounter_ended == False:
#         userinput = input('> ')
#         # Player's turn
#         # Attack
#         if userinput == 'a':
#             damage = weapon.damage
#             enemy.hitpoints = enemy.hitpoints - damage 
#             if enemy.hitpoints <= 0:
#                 print(enemy.name + ' was slain! You venture on...')
#                 encounter_ended = True
#             else:
#                 print('You hit the ' + enemy.name + ' for ' + str(damage) + '! It has ' + str(enemy.hitpoints) + ' HP left.')

#         # Healing potion
#         elif userinput == 'h': 
#             mainchar.hitpoints = mainchar.hitpoints + 25
#             print('The healing potion gives you +25HP. ' + str(mainchar.hitpoints) + ' HP remaining.')

#         # Enemy's turn
#         if encounter_ended == False:
#             mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damge
#             print(enemy.name + ' hit you for ' + str(enemy.enemy_damge) + ' damage. ' + str(mainchar.hitpoints) + '/100 HP remaining.')

