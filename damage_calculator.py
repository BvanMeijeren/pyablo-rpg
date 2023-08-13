# critical hit function that can be applied to any skill in the game
import random

def damage_calculator(caster,target, fire_dmg,ice_dmg,electricity_dmg):    
    crit = random.randint(0,100) < caster.critical_chance
    
    # elemental defense
    damage_elemental_def_applied = (fire_dmg * target.fire_def + 
                                    ice_dmg * target.ice_def + 
                                    electricity_dmg * target.electricity_def
                                    )

    # critical hits
    if crit == True:
        print(caster.name + ' had a critical hit! Damage X' + str(caster.critical_multiplier) + '' )
        damage_dealt = (damage_elemental_def_applied * caster.critical_multipler)
    else:
        damage_dealt = damage_elemental_def_applied

    return damage_dealt