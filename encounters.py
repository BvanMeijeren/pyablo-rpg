from enemies import enemies
from spells import *
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
    print_slow('A ' + enemy.name + ' (' + str(enemy.hitpoints) +' HP) has appeared!')
    print(keybindings)
    
    # encounter instance
    while encounter_ended == False and userinput != 'q':
        # Determine enemy action
        enemy_action = random.choice(spells) # random pick from skill dict keys
        print_slow(enemy.name + ' will use ' + enemy_action + ' next turn. What will you do?')

        # Player's turn
        player_turn_over = False
        # Boolean to determine if player is still alive
        you_are_dead = False
        # Initial user input for player's turn
        userinput = input('> ')

        if userinput != 'q':
            while player_turn_over == False:
                exec(keybindings[userinput]+'(mainchar, enemy, weapon)') # execute selected player action
                if userinput in ['h','i','c','e']:
                    userinput = input('> ')
                else:
                    player_turn_over = True
        else:
            encounter_ended = True

        # Check if enemy died
        if enemy.hitpoints <= 0:
            print_slow(enemy.name + ' was slain, which increased your XP by '+ str(enemy.xp) + '! You venture on...')
            encounter_ended = True
            mainchar.xp = mainchar.xp + enemy.xp # xp reward

        # Enemy's turn
        if encounter_ended == False and userinput != 'q':
            exec(enemy_action+'(enemy,mainchar,weapon)')

        # check if player died
        if mainchar.hitpoints <= 0:
            encounter_ended= True 
            print('Lol, you have been pwned by a ' + enemy.name + '. Try again.')
            you_are_dead = True
            
    return you_are_dead
            

