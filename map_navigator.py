from mapgenerator import *

def navigate_map(map_structure, trail):
    # determine current player position in map
    nr_choices_made = max(list(trail.keys()))
    last_decision = trail[max(list(trail.keys()))] # last element of trail list
    #current_pos = map_structure[nr_choices_made-1] 
    if nr_choices_made < len(map_structure):
        nr_options_next_turn = map_structure[nr_choices_made+1]
    else:
        nr_options_next_turn = -1

    # Give player available options
    available_options = []

    if last_decision in [1,3]:
        if nr_options_next_turn in [2,3]:
            available_options = available_options.append([])

    print(available_options)

#navigate_map([1,2,3,1], {0:2,1:1})