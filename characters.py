class Character:
    def __init__(self, name, enemy_damge, level, hitpoints, species, fire_def, ice_def, electricity_def):
        self.name = name 
        self.level = level
        self.hitpoints = hitpoints
        self.species = species
        self.fire_def = fire_def
        self.ice_def = ice_def
        self.electricity_def = electricity_def
        self.enemy_damge = enemy_damge


# class Enemy(Character):
#     def __init__(self, damage):
#         self.damage = damage


