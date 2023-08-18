import random
from colorama import Fore, Back, Style

def generate_map(mainchar):
    # map length determines the number of moves the player have to make before entering the next map
    map_length = mainchar + 5

    map_structure = {}
    for i in range(1,map_length):
        map_structure[i] = 'default'

    # based on player level, determine how many decision there will be
    decisions = random.randint(1,round(map_length*0.2))
    decision_indices = []

    # set positions of the events
    for i in range(decisions):
        pos = random.randint(2,map_length) # first position cannot be split
        map_structure[pos] = 'event'

    return map_structure


print(generate_map(2))

def visualize_map(map_structure):
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    fifth_line = ''

    lines = [first_line, second_line, third_line, fourth_line, fifth_line]

    # player trail through map
    trail = {2:1}

    index = 1
    for i in map_structure:
        if i == 1:
            lines = [item + '  ' for item in lines]
            lines[2] = lines[2][:-2] + ' O' # only third line gets node
        if i == 2:
            lines[0] = lines[0] + ' O'
            lines[1] = lines[1] + '  '
            lines[2] = lines[2] + '  '
            lines[3] = lines[3] + '  '
            lines[4] = lines[4] + ' O'
        if i == 3:
            lines[0] = lines[0] + ' O'
            lines[1] = lines[1] + '  '
            lines[2] = lines[2] + ' O'
            lines[3] = lines[3] + '  '
            lines[4] = lines[4] + ' O'

        if index == 2:
            lines[0] = lines[0][:-1] + 'X'
        index += 1

    # draw vertices
    # draw ascending vertices
    for i in range(len(lines[2])-2):
        if lines[2][i] in ['O','X'] and lines[0][i+2] in ['O','X']: #and lines[0][i] != 'O':
            lines[1] = lines[1][:i+1] + '/' + lines[1][i:]
            lines[3] = lines[3][:i+1] + '\\' + lines[3][i:]
    # draw descending vertices
    for i in range(2,len(lines[2])):
        if lines[2][i] in ['O', 'X'] and lines[0][i-2] in ['O', 'X'] and lines[0][i] not in ['O', 'X']:
            lines[1] = lines[1][:i-1] + '\\' + lines[1][i:]
            lines[3] = lines[3][:i-1] + '/' + lines[3][i:]
        
    # Insert End text = player position
    lines[2] = (lines[2] + Fore.RED + ' END' + Style.RESET_ALL + 
                '            Your are here: ' + Fore.YELLOW + 'X' + Style.RESET_ALL)

    # draw player trail

    for i in range(len(lines)):
        lines[i] = lines[i].replace('O O', 'O-O').replace('O O', 'O-O').replace('X O', 'X-O').replace('O X', 'O-X')

        # add start text
        if i == 2:
            lines[i] = Fore.GREEN + 'Start' + Style.RESET_ALL + lines[i] 
        else:
            lines[i] = '     ' + lines[i]
        
        # print lines one by one
        print(lines[i])


visualize_map([1,3,2,1,2,1,1,3,1,1,1])