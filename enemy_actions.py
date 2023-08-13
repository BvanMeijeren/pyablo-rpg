# List of skills enemies can use
# Which enemy can use what is determined through an Class attribute called skills, which is a list of names

enemy_actions = ['niffle', 'fireball', 'ice_shield']

def niffle(mainchar,enemy,weapon):
    print(enemy.name +' used Niffle! It hits you for ' + str(enemy.enemy_damage) + '.')
    mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damage

def fireball(mainchar,enemy,weapon):
    print(enemy.name +' used Fireball! It hits you for ' + str(enemy.enemy_damage) + '.')
    mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damage

def ice_shield(mainchar,enemy,weapon):
    print(enemy.name +' used Ice Shield! Damage reduced for 20%.')
    mainchar.hitpoints = mainchar.hitpoints - enemy.enemy_damage

