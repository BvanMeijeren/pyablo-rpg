class Character:
    #stats
    def __init__(self, name, enemy_damge, level, xp, hitpoints, species, fire_def, ice_def, electricity_def, skills):
        self.name = name 
        self.level = level
        self.xp = xp # for enemies, this is how much you gain upon slaying them
        self.hitpoints = hitpoints
        self.species = species
        self.fire_def = fire_def
        self.ice_def = ice_def
        self.electricity_def = electricity_def
        self.enemy_damge = enemy_damge # enemy attribute
        self.skills = skills


# class Enemy(Character):
#     def __init__(self, damage):
#         self.damage = damage


