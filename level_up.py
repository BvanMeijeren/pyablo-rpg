from Pyablo import mainchar

# Check if level up
def level_up(mainchar):
    if mainchar.xp >= 100:
        mainchar.level = mainchar.level + 1
        print('Your level increased by 1, you are now level ' + str(mainchar.level) + '!')