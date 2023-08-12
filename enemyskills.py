# List of skills enemies can use
# Which enemy can use what is determined through an Class attribute called skills, which is a list of names

def niffle(mainchar,enemy,weapon):
    print(enemy.name +' used Niffle! It hits you for ' + str(enemy.damage) + '.')
    mainchar.hitpoints = mainchar.hitpoints - enemy.damage