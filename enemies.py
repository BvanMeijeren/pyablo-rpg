from characters import *
from colorama import Fore, Back, Style
import random

# Skeleton
def create_skeleton(mainchar, weapon):
    skeleton = Character(
        name = Fore.RED + 'Broken Skeleton' + Style.RESET_ALL,
        id = 'skeleton', # used to match the right image
        level = mainchar.level,
        xp =50,
        hitpoints = random.randint(18,30), 
        critical_chance= 20,
        critical_multiplier=2,
        species = 'Skeleton',
        fire_def=-30,
        ice_def=20,
        electricity_def=40,
        enemy_damage=10,
        skills=[],
        items={'Health Potions': 0},
        equipped_weapon=None,
        profession=''
        )
    
    return skeleton

# Ice elemental
def create_ice_elemental(mainchar,weapon):
    ice_elemental = Character(
        name = Fore.RED + 'Ice Elemental' + Style.RESET_ALL,
        id = 'ice_elemental',
        level = mainchar.level,
        xp = 50,
        hitpoints = random.randint(18,30), 
        critical_chance= 20,
        critical_multiplier=2,
        species = 'Elemental',
        fire_def=-100,
        ice_def=100,
        electricity_def=50,
        enemy_damage= 12,
        skills=[],
        items={'Health Potions': 0},
        equipped_weapon=None,
        profession=''
        )
    
    return ice_elemental

# Goblin
def create_goblin(mainchar,weapon):
    goblin = Character(
        name = Fore.RED + 'Goblin Intern' + Style.RESET_ALL,
        id = 'goblin',
        level = 1,
        xp = 50,
        hitpoints = 25, 
        critical_chance= 20,
        critical_multiplier=2,
        species = 'Goblin',
        fire_def=-50,
        ice_def=30,
        electricity_def=0,
        enemy_damage= 8,
        skills = ['niffle'],
        items={'Health Potions': 0},
        equipped_weapon=None,
        profession=''
        )
    
    return goblin

enemies = [create_skeleton, create_ice_elemental, create_goblin]

