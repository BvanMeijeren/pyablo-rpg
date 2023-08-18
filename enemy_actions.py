from graphics import *
from damage_calculator import *

def niffle(caster,target,weapon):
    if target.items['Health Potions'] > 0: 
        target.items['Health Potions'] -= 1
        print_slow(caster.name +' used Niffle and stole a Health Potion! ' + str(caster.items['Health Potions']) + ' potions left.')
    else:
        print(target.name + ' has no Health Potions left.')

def fireball(caster,target,weapon):
    physical_dmg = 0
    fire_dmg = 12
    ice_dmg = 0
    electricity_dmg = 0

    damage = damage_calculator(caster, target, physical_dmg, fire_dmg, ice_dmg, electricity_dmg)
    target.hitpoints = target.hitpoints - damage
    print_slow(caster.name +' used Fireball on you for ' + str(damage) + ' damage. ' + str(target.hitpoints) + ' HP remaining.')


def ice_shield(caster,target,weapon):
    caster.hitpoints = caster.hitpoints - target.enemy_damage
    print_slow(target.name +' used Ice Shield. Damage reduced by 30%.')

# list of all skills' function names
spells = [k for k in dir() if '__' not in k]