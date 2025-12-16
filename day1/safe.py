
# file_path = "./input-full.txt"
file_path = "./input.txt"
initial_dial_pos = 50
total_dial = 100

current_dial_position = initial_dial_pos

number_of_zeros = 0
counter = 0
total_clicks = 0

def read_file_lines(file_path):
    # Initialize an empty list to store lines
    lines = []

    try:
        # Open the file in read mode using 'with' statement
        with open(file_path, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Remove trailing newline character and add the line to the list
                lines.append(line.strip())
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)

    return lines

lines = read_file_lines(file_path)

# Print the lines stored in the list
for line in lines:
   
    cycle_clicks = 0
    counter += 1
    direction = line[0]
    rotation = int(line[1:])

    # print(f"dir: {direction}, rotation: {rotation}")
    current_dial_position_pre_rotation = current_dial_position
    print(f"initial dial position for cycle: {current_dial_position_pre_rotation}")

    if direction == 'L':
        new_rotation = -rotation
    else:
        new_rotation = rotation

    current_dial_position = current_dial_position+new_rotation
    current_dial_position_pre_count = current_dial_position
    cycle_clicks = int(current_dial_position_pre_count/100)

    current_dial_position = current_dial_position%100
    
    # single rotation, skip counting
    if current_dial_position == 0:
        print("dial position at 0")
        cycle_clicks += 1
        pass
    elif current_dial_position_pre_count < current_dial_position_pre_rotation:
        print(f"less than: {cycle_clicks}, {int(current_dial_position_pre_count/100)}")
        cycle_clicks += 1
        if abs(int(current_dial_position_pre_count/100)) > 0:
            print("multiple rotations, add +1 click")
            cycle_clicks += abs(int(current_dial_position_pre_count/100))
    elif current_dial_position_pre_count > current_dial_position_pre_rotation:
        print(f"greater than: {cycle_clicks} {int(current_dial_position_pre_count/100)}")
        cycle_clicks += 1
        if abs(int(current_dial_position_pre_count/100)) > 0:
            print("multiple rotations, add +1 click")
            cycle_clicks += abs(int(current_dial_position_pre_count/100))

    # if current_dial_position == 0:
    #     cycle_clicks += 1


    total_clicks += cycle_clicks


    print(f"rotation #{counter}: {new_rotation}")
    print(f"dial position: {current_dial_position}")
    print(f"current dial position pre count: {current_dial_position_pre_count}, cycle clicks: {cycle_clicks}")
    print("- - - -")

print(f"total zeros: {number_of_zeros}")
print(f"total clicks: {total_clicks}")





