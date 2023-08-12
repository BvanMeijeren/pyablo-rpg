# To add a function: add a function like the others and add the keybinding

# keybindings
keybindings = {
    '1': 'attack',
    '2': 'healing_potion',
    '3': 'defend',
    'h': 'help'
}

# all the first letters of the function names should be unique!
# all functions should use mainchar, weapon and enemy as parameters
def healing_potion(mainchar,enemy,weapon):
    mainchar.hitpoints = mainchar.hitpoints + 25
    print('You used a healing potion. It gives you +25HP! You now have ' + str(mainchar.hitpoints) + ' HP.' )

def attack(mainchar, enemy, weapon):
    enemy.hitpoints = enemy.hitpoints - weapon.damage 
    if enemy.hitpoints <=0:
        print('You hit the ' + enemy.name + ' for ' + str(weapon.damage) )
    else:
        print('You hit the ' + enemy.name + ' for ' + str(weapon.damage) + '! It has ' + str(enemy.hitpoints) + ' HP left.')

def defend(mainchar,enemy,weapon):
    print('You brace yourself for the next hit, reducing its damage by 50% -- WIP!')

def help(mainchar,enemy,weapon):
    print(keybindings)

