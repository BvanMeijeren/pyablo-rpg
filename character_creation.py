from characters import Character
from weapons import *

# Character creation
def character_creation():
    print('Choose your hero by answering the following questions:')
    name = input('What is your hero\'s name?')
    species = input('Are you an human, elf, dwarf')

    print('Creating character...')
    # character creation with base stats
    mainchar = Character(
        name = name, 
        species = species,
        electricity_def = 25, 
        hitpoints = 100, 
        fire_def =25, 
        ice_def=25, 
        level=1,
        enemy_damge=0)

    print('Character created!')
    return mainchar

# Start weapon
def create_starterweapon():
    import random 
    weapontype = random.choice(weapontypes)
    starterweapon = Weapon(
        name = 'Noob ' + weapontype,
        damage = 8,
        type = weapontype,
        critical_chance = 0.1,
        is_two_handed = False,
        fire_dmg_prop=0,
        electricity_dmg_prop=0,
        ice_dmg_prop=0,
        skeleton_dmg_bonus= 1.1,
        goblin_dmg_bonus=1.2
    )
    return starterweapon