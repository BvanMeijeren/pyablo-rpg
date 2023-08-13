from characters import *
import random

# Skeleton
def create_skeleton(mainchar, weapon):
    skeleton = Character(
        name = 'Broken Skeleton',
        id = 'skeleton', # used to match the right image
        level = mainchar.level,
        xp =50,
        hitpoints = random.randint(18,30), 
        critical_chance= 20,
        critical_multiplier=2,
        species = 'Skeleton',
        fire_def=0,
        ice_def=20,
        electricity_def=40,
        enemy_damage=weapon.damage * 0.5,
        skills=[],
        items={}
        )
    
    return skeleton

# Ice elemental
def create_ice_elemental(mainchar,weapon):
    ice_elemental = Character(
        name = 'Ice Elemental',
        id = 'ice_elemental',
        level = mainchar.level,
        xp = 50,
        hitpoints = random.randint(18,30), 
        critical_chance= 20,
        critical_multiplier=2,
        species = 'Elemental',
        fire_def=0,
        ice_def=80,
        electricity_def=40,
        enemy_damage= weapon.damage*0.6,
        skills=[],
        items={}
        )
    
    return ice_elemental

# Goblin
def create_goblin(mainchar,weapon):
    goblin = Character(
        name = 'Goblin Intern',
        id = 'goblin_intern',
        level = 1,
        xp = 50,
        hitpoints = 25, 
        critical_chance= 20,
        critical_multiplier=2,
        species = 'Goblin',
        fire_def=0,
        ice_def=80,
        electricity_def=40,
        enemy_damage=weapon.damage*0.4,
        skills = ['niffle'],
        items={}
        )
    
    return goblin

enemies = [create_skeleton, create_ice_elemental, create_goblin]

