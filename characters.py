class Character:
    #stats
    def __init__(self, name, id, enemy_damage, level, xp, hitpoints, critical_chance, critical_multiplier, species, 
                 fire_def, ice_def, electricity_def, skills, items, equipped_weapon, profession):
        self.name = name 
        self.id = id
        self.level = level
        self.xp = xp # for enemies, this is how much you gain upon slaying them
        self.hitpoints = hitpoints
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier
        self.species = species
        self.fire_def = fire_def # from -100 to 100 percent
        self.ice_def = ice_def # from -100 to 100 percent
        self.electricity_def = electricity_def # from -100 to 100 percent
        self.enemy_damage = enemy_damage # enemy attribute
        self.skills = skills
        self.items = items # hero's items
        self.equipped_weapon = equipped_weapon
        self.profession = profession


# class Enemy(Character):
#     def __init__(self, damage):
#         self.damage = damage


