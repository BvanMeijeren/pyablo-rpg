class Weapon:
  def __init__(self, name, damage, type, is_two_handed, fire_dmg_prop, ice_dmg_prop, electricity_dmg_prop, skeleton_dmg_bonus, goblin_dmg_bonus):
    self.name = name
    self.damage = damage
    self.type = type
    #self.critical_chance = critical_chance
    self.is_two_handed = is_two_handed
    self.fire_dmg_prop = fire_dmg_prop
    self.ice_dmg_prop = ice_dmg_prop
    self.electricity_dmg_prop = electricity_dmg_prop
    self.skeleton_dmg_bonus = skeleton_dmg_bonus
    self.goblin_dmg_bonus = goblin_dmg_bonus

weapontypes = ['Staff','Axe','Sword','Flail','Spear','Mace']
