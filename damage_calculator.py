# critical hit function that can be applied to any skill in the game
import random

def damage_calculator(caster,target, physical_dmg, fire_dmg, ice_dmg, electricity_dmg):    
    crit = random.randint(0,100) < caster.critical_chance
    
    # elemental defense
    damage_elemental_def_applied = (physical_dmg + 
                                    fire_dmg * (1-target.fire_def/100) + 
                                    ice_dmg * (1-target.ice_def/100) + 
                                    electricity_dmg * (1-target.electricity_def/100)
                                    )

    # critical hits
    if crit == True:
        print(caster.name + ' had a critical hit! Damage X' + str(caster.critical_multiplier) + '' )
        damage_dealt = (damage_elemental_def_applied * caster.critical_multiplier)
    else:
        damage_dealt = damage_elemental_def_applied

    return damage_dealt