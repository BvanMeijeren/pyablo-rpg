from enemies import enemies
from enemy_actions import *
from graphics import *
import random 
import os
from player_actions import *

# encounter function
def encounter(mainchar, weapon, userinput):

    # determine enemy and set encounter game state
    enemy = random.choice(enemies)(mainchar, weapon)
    encounter_ended = False

    # print enemy ASCII image
    print(show_enemy(enemy.id))
    # encounter intro + options
    print_slow('A ' + enemy.name + ' has appeared!')
    print(keybindings)
    
    # encounter instance
    while encounter_ended == False and userinput != 'q':
        # Determine enemy action
        enemy_action = random.choice(enemy_actions)
        print_slow(enemy.name + ' will use ' + enemy_action + ' next turn. What will you do?')

        
        userinput = input('> ')

        # Player's turn
        if userinput != 'q':
            exec(keybindings[userinput]+'(mainchar, enemy, weapon)') # execute selected player action
        else:
            encounter_ended = True

        # Check if enemy died
        if enemy.hitpoints <= 0:
            print_slow(enemy.name + ' was slain, which increased your XP by '+ str(enemy.xp) + '! You venture on...')
            encounter_ended = True
            mainchar.xp = mainchar.xp + enemy.xp # xp reward

        # Enemy's turn
        if encounter_ended == False and userinput != 'q':
            exec(enemy_action+'(mainchar,enemy,weapon)')
            #print_slow(enemy.name + ' hit you for ' + str(round(enemy.enemy_damage)) + ' damage. ' + str(round(mainchar.hitpoints)) + ' HP remaining.')

