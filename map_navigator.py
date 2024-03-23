from mapgenerator import *

def navigate_map(map_structure, trail):
    # determine current player position in map
    nr_steps_made = max(list(trail.keys()))
    current_position = trail[max(list(trail.keys()))] # last element of trail list
    current_step = map_structure[nr_steps_made] 
    next_pos_nodes = map_structure[nr_steps_made+1]

    # Give player available options depending on their current position and next available positions
    available_options = [1,2,3]

    # Generate available options for navigation
    if current_position == 1:
        available_options = [1,2]
        if next_pos_nodes == 1:
            available_options = [2]
        if next_pos_nodes == 2:
            available_options = [1]

    if current_position == 3:
        available_options = [2,3]
        if next_pos_nodes == 1:
            available_options = [2]
        if next_pos_nodes == 2:
            available_options = [3]

    if current_position == 2:
        available_options = [1,2,3]
        if next_pos_nodes == 1:
            available_options = [2]
        if next_pos_nodes == 2:
            available_options = [1,3]
    
    # Generate navigation question for user
    nav_options_string = ''
    nr_of_options_presented = len(available_options)
    count = 1
    for i in available_options:
        if nr_of_options_presented == count and nr_of_options_presented > 1:
            nav_options_string = nav_options_string + 'or ' + str(i)
        else:
            nav_options_string = nav_options_string + str(i) + ' '
        count += 1

    visualize_vertical_map(map_structure, trail)
    print('Choose your next path: Will it be path ' + nav_options_string + '?')
    next_step = input('> ')

    # add the new step to the player's trail
    trail[current_step] = int(next_step)

    print(trail)
    visualize_vertical_map(map_structure, trail)

navigate_map([1,2,3,2,3,1], {0:2,1:3,2:2})