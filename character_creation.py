from characters import Character
from weapons import *

# Character creation
def character_creation():
    print('Choose your hero by answering the following questions:')
    print('What is your hero\'s name?')
    name = input('> ')
    print('Are you an human, elf, dwarf?')
    species = input('> ')

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
        xp=0,
        enemy_damge=0,
        skills=[]
        )

    print('Character created!')
    return mainchar

# Start weapon
def create_starterweapon():
    import random 
    weapontype = random.choice(weapontypes)
    starterweapon = Weapon(
        name = 'Noob ' + weapontype,
        damage = random.randint(8, 12),
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