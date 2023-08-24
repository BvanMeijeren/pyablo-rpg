import random
from colorama import Fore, Back, Style

def generate_map_structure(mainchar):
    # map length determines the number of moves the player have to make before entering the next map
    map_length = mainchar.level + 5

    map_structure = [] # indicates for every position in the map how many options there are/were

    # default value for the 
    for i in range(1,map_length):
        map_structure[i] = 1 # default single path 

    # based on player level, determine how many decision there will be
    decisions = random.randint(1,round(map_length*0.2))

    # set positions of the events
    for i in range(decisions):
        pos = random.randint(2,map_length) # first position cannot be split
        map_structure[pos] = random.randint(2,3)

    return map_structure

def visualize_vertical_map(map_structure, player_trail):
    
    vertices = []

    # add vertices
    for i in map_structure:
        if i == 1:
            vertices.append('  O  ')
        elif i == 2:
            vertices.append('O   O')
        elif i == 3:
            vertices.append('O O O')

    # correct indices of player trail so that choice places match string indices
    for key,value in player_trail.items():
        if value == 1:
            player_trail[key] = 0
        elif value == 3:
            player_trail[key] = 4


    # Visualize player position X (without colors, because those mess up the edges)
    current_pos = max(list(player_trail.keys()))
    current_node = player_trail[current_pos]

    vertices[current_pos] = vertices[current_pos][:current_node] + 'X' + vertices[current_pos][current_node+1:]

    edges = []

    # add edges
    for index in range(len(map_structure)-1):

        line_to_be_added = '     '

        # get all indices for vertices in strings
        prev_vertices = [i for i, ltr in enumerate(vertices[index]) if ltr in ['O', 'X']]
        next_vertices = [i for i, ltr in enumerate(vertices[index+1]) if ltr in ['O','X']]

        for y in prev_vertices:
            if y in next_vertices:
                line_to_be_added = line_to_be_added[:y] + '|' + line_to_be_added[y+1:]
            if y + 2 in next_vertices:
                line_to_be_added = line_to_be_added[:y+1] + '\\' + line_to_be_added[y+2:]
            if y - 2 in next_vertices:
                line_to_be_added = line_to_be_added[:y-1] + '/' + line_to_be_added[y:]

        edges.append(line_to_be_added)

    edges.append('')

    # print the colored map
    print(Fore.GREEN + 'START' + Style.RESET_ALL)
    for i in range(len(vertices)):
        # color the map
        if i in list(player_trail.keys()):
            player_choice = player_trail[i]
            to_be_printed_line = vertices[i]
            vertices[i] = (to_be_printed_line[:player_choice] + Fore.BLUE + to_be_printed_line[player_choice] 
                           + Style.RESET_ALL + to_be_printed_line[player_choice+1:])

        print(vertices[i])
        if i < len(edges) and edges[i] != '':
            print(edges[i])

    print(' ' + Fore.RED + 'BOSS' + Style.RESET_ALL)

visualize_vertical_map([1,2,3,1], {0:2,1:1,2:1})