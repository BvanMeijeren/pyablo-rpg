import random
from weapongenerator import generate_weapon

#Generate loot
def generate_loot(mainchar):
    #dropped_loot = []

    # Weapon drops
    weapon_drop_rate = 100 # percentage
    weapon_drop_bool = random.randrange(100) < weapon_drop_rate

    if weapon_drop_bool == True:
        dropped_weapon = generate_weapon(mainchar)
        print('You have found a ' + dropped_weapon.name + '! Go to your inventory to equip it.')
        #dropped_loot = dropped_loot.append(dropped_weapon)
        mainchar.items.update({dropped_weapon: 1})

    # Health potion drop
    health_potion_drop_rate = 20
    health_potion_drop_bool = random.randrange(100) < weapon_drop_rate

    if health_potion_drop_bool == True:
        mainchar.items['Health Potions'] += int(1) # add one potion
        print('You have found a Health Potion!')
