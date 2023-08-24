from mapgenerator import *

def navigate_map(map_structure, trail):
    # determine current player position in map
    nr_choices_made = len(trail)
    last_decision = trail[:-1] # last element of trail list
    current_pos = map_structure[nr_choices_made-1]
    nr_options_next_turn = map_structure[nr_choices_made]

    # Give player available options
    available_options = []
    # position = 2, last decision = 3 --> 2 & 3
    # 2,1 --> 
    if last_decision in [1,3]:
        if nr_options_next_turn in [2,3]:
            available_options = available_options.append([])