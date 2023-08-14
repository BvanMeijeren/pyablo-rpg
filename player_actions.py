from weapons import *
from graphics import *
from damage_calculator import *
from spells import *
import random

# To add a function: add a function like the others and add the keybinding

# keybindings
keybindings = {
    '1': 'attack',
    '2': 'defend',
    '3': 'cast_spell',
    '4': 'healing_potion',
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
    damage_calculated = damage_calculator(mainchar, enemy, weapon.physical_dmg, 
                                          weapon.fire_dmg, weapon.ice_dmg, weapon.electricity_dmg)
    enemy.hitpoints = enemy.hitpoints - damage_calculated

    if enemy.hitpoints <=0:
        print_slow('You hit the ' + enemy.name + ' for ' + str(damage_calculated) + '.')
    else:
        print_slow('You hit the ' + enemy.name + ' for ' + str(damage_calculated) + '! It has ' + str(enemy.hitpoints) + ' HP left.')


def cast_spell(mainchar,enemy,weapon):
    spell = input('Spell:')
    print(spell)
    exec(spell + '(mainchar,enemy,weapon)')


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
    from pprint import pprint
    pprint(vars(enemy))
