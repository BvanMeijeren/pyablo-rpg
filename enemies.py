from characters import *

# Skeleton
skeleton = Character(
    name = 'Broken Skeleton',
    level = 1,
    hitpoints = 20, 
    species = 'Skeleton',
    fire_def=0,
    ice_def=20,
    electricity_def=40,
    enemy_damge=6)

# Ice elemental
ice_elemental = Character(
    name = 'Ice Elemental',
    level = 1,
    hitpoints = 30, 
    species = 'Elemental',
    fire_def=0,
    ice_def=80,
    electricity_def=40,
    enemy_damge=10)

# Goblin
goblin = Character(
    name = 'Goblin Intern',
    level = 1,
    hitpoints = 25, 
    species = 'Goblin',
    fire_def=0,
    ice_def=80,
    electricity_def=40,
    enemy_damge=6)

enemies = [skeleton, ice_elemental, goblin]