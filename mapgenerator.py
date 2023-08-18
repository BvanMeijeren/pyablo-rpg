import random

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

    index = 1
    for i in map_structure:
        print(i)
        if i == 1 or i == 3:
            third_line = third_line + ' O'
        
        if i == 2 or i == 3:
            first_line = first_line + ' O'
            fifth_line = fifth_line + ' O'

        max_length_line = len(max(lines, key=len))

        for j in lines:
            if len(j) < max_length_line:
                lines[j] = j + '  '

    print(fourth_line)
    # for i in drawing:
    #     print(i)



visualize_map([1,1,2,3,1])