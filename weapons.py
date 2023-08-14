class Weapon:
  def __init__(self, name, type, is_two_handed, physical_dmg, fire_dmg, ice_dmg, electricity_dmg, skeleton_dmg_bonus, goblin_dmg_bonus):
    self.name = name
    self.type = type
    #self.critical_chance = critical_chance
    self.is_two_handed = is_two_handed
    self.physical_dmg = physical_dmg
    self.fire_dmg = fire_dmg
    self.ice_dmg = ice_dmg
    self.electricity_dmg = electricity_dmg
    self.skeleton_dmg_bonus = skeleton_dmg_bonus
    self.goblin_dmg_bonus = goblin_dmg_bonus

weapontypes = ['Staff','Axe','Sword','Flail','Spear','Mace']
