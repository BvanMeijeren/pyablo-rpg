from weapons import *
from graphics import *
import random

# To add a function: add a function like the others and add the keybinding

# keybindings
keybindings = {
    '1': 'attack',
    '2': 'healing_potion',
    '3': 'defend',
    'h': 'help',
    'i': 'inventory',
    'c': 'character_stats',
    'e': 'inspect_enemy'
}

# all the first letters of the function names should be unique!
# all functions should use mainchar, weapon and enemy as parameters
def healing_potion(mainchar,enemy,weapon):
    mainchar.hitpoints = mainchar.hitpoints + 25 
    print_slow('You used a healing potion. It gives you +25HP! You now have ' + str(mainchar.hitpoints) + ' HP.' )

def attack(mainchar, enemy, weapon):
    crit = random.randint(0,100) < mainchar.critical_chance
    if crit == True:
        print('Critical hit! Damage X' + str(mainchar.critical_multiplier) + '!')
        enemy.hitpoints = enemy.hitpoints - (weapon.damage * mainchar.critical_multiplier)
    elif crit == False:
        enemy.hitpoints = enemy.hitpoints - weapon.damage

    if enemy.hitpoints <=0:
        print_slow('You hit the ' + enemy.name + ' for ' + str(weapon.damage) + '.')
    else:
        print_slow('You hit the ' + enemy.name + ' for ' + str(weapon.damage) + '! It has ' + str(enemy.hitpoints) + ' HP left.')

def defend(mainchar,enemy,weapon):
    print_slow('You brace yourself for the next hit, reducing its damage by 50% -- WIP!')

def help(mainchar,enemy,weapon):
    print(keybindings)

def inventory(mainchar,enemy,weapon):
    print_slow('--------------')
    for key, value in mainchar.items.items():
        # if items is of weapon class, print_slow its name, otherwise print_slow key
        if isinstance(key, Weapon):
            print_slow(key.name)
        else:
            print_slow(key + ': ' + str(value))
    
    print_slow('--------------')

def character_stats(mainchar,enemy,weapon):
    from pprint import pprint
    pprint(vars(mainchar))

def inspect_enemy(mainchar,enemy,weapon):
    from pprint import pprint_slow
    pprint_slow(vars(enemy))
