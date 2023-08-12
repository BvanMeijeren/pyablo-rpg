from characters import *
import random

# Skeleton
def create_skeleton(mainchar):
    skeleton = Character(
        name = 'Broken Skeleton',
        level = mainchar.level,
        xp =7,
        hitpoints = random.randint(18,30), 
        species = 'Skeleton',
        fire_def=0,
        ice_def=20,
        electricity_def=40,
        enemy_damge=mainchar.damage * 0.5
        )
    
    return skeleton

# Ice elemental
def create_ice_elemental(mainchar):
    ice_elemental = Character(
        name = 'Ice Elemental',
        level = mainchar.level,
        xp = 10,
        hitpoints = random.randint(18,30), 
        species = 'Elemental',
        fire_def=0,
        ice_def=80,
        electricity_def=40,
        enemy_damge=10
        )
    
    return ice_elemental

# Goblin
def create_goblin(mainchar):
    goblin = Character(
        name = 'Goblin Intern',
        level = 1,
        xp = 6,
        hitpoints = 25, 
        species = 'Goblin',
        fire_def=0,
        ice_def=80,
        electricity_def=40,
        enemy_damge=6,
        skill = ['niffle']
        )
    
    return goblin

enemies = [create_skeleton, create_ice_elemental, create_goblin]