from graphics import *
from damage_calculator import *

# List of skills enemies can use
# Which enemy can use what is determined through an Class attribute called skills, which is a list of names

enemy_actions = ['niffle', 'fireball', 'ice_shield']

# Default attack action for enemies
def attack(caster,target,weapon):    
    crit = random.randint(0,100) < caster.critical_chance
    
    if crit == True:
        print(target.name + ' had a critical hit on you! Damage X' + str(target.critical_multiplier) + '!' )
        caster.hitpoints = caster.hitpoints - (target.enemy_damage * target.critical_multipler)
    else:
        caster.hitpoints = caster.hitpoints - target.enemy_damage
    
    print_slow(target.name +' attacked you for ' + str(target.enemy_damage) + ' damage. ' + str(caster.hitpoints) + ' HP remaining.')


def niffle(caster,target,weapon):
    caster.items['Health Potions'] -= 1
    print_slow(target.name +' used Niffle and stole one of your Health Potions! You have ' + str(caster.items['Health Potions']) + ' left.')

def fireball(caster,target,weapon):
    fire_dmg = 8
    ice_dmg = 0
    electricity_dmg = 0

    damage = damage_calculator(caster, target, fire_dmg, ice_dmg, electricity_dmg)
    target.hitpoints = target.hitpoints - damage
    print_slow(caster.name +' used Fireball on you for ' + str(damage) + ' damage. ' + str(target.hitpoints) + ' HP remaining.')


def ice_shield(caster,target,weapon):
    caster.hitpoints = caster.hitpoints - target.enemy_damage
    print_slow(target.name +' used Ice Shield. Damage reduced by 30%.')


