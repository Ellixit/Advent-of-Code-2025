
def find_paper_rolls():

    rows_list   = []
    valid_rolls = 0
    
    with open("day-04-input.txt", "r") as file:
        rows_list = [row.rstrip("\n") for row in file]

    while True:
        temp         = calculate_adjacency(rows_list)
        valid_rolls += temp

        for row in rows_list:
            print(row)
        
        print(valid_rolls, end="\n\n")
        
        if temp == 0:
            break
        
    print(f"{valid_rolls}")
    
def calculate_adjacency(rows_list):
    
    num_rows    = len(rows_list)
    current_row = 0
    valid_rolls = 0
    
    for row in rows_list:
        
        # Determine if need to check rows above and below
        above_row   = current_row - 1
        below_row   = current_row + 1
        check_above = True
        check_below = True
    
        if above_row < 0:
            check_above = False
            
        if below_row >= num_rows:
            check_below = False
    
        roll_index = 0
        
        indices_to_remove = []
    
        for roll in row:
            
            if roll != '@':
                roll_index += 1
                continue

            # Determine if need to check left and right
            left_index  = roll_index - 1
            right_index = roll_index + 1
            check_left  = True
            check_right = True
            
            if left_index < 0:
                check_left = False
                
            if right_index >= len(row):
                check_right = False
                
            num_adjacent_rolls = 0
                
            # Check row above current
            if check_above:
                num_adjacent_rolls += 1 if rows_list[above_row][roll_index] == '@' else 0
                
                if check_left:
                    num_adjacent_rolls += 1 if rows_list[above_row][left_index] == '@' else 0
                    
                if check_right:
                    num_adjacent_rolls += 1 if rows_list[above_row][right_index] == '@' else 0

            # Check row below current
            if check_below:
                num_adjacent_rolls += 1 if rows_list[below_row][roll_index] == '@' else 0
                
                if check_left:
                    num_adjacent_rolls += 1 if rows_list[below_row][left_index] == '@' else 0
                    
                if check_right:
                    num_adjacent_rolls += 1 if rows_list[below_row][right_index] == '@' else 0
                    
            # Check position to left
            if check_left:
                num_adjacent_rolls += 1 if row[left_index] == '@' else 0

            # Check position to right
            if check_right:
                num_adjacent_rolls += 1 if row[right_index] == '@' else 0
                
            if num_adjacent_rolls < 4:
                valid_rolls += 1
                indices_to_remove.append(roll_index)
                
            roll_index += 1
            
        new_row = row
            
        for index in indices_to_remove:
            new_row = new_row[:index] + 'X' + new_row[index + 1:]
        
        rows_list[current_row] = new_row
        
        current_row += 1

    return valid_rolls
 
find_paper_rolls()