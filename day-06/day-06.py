
def solve_math_homework():
    
    rows  = []
    
    with open("day-06-input.txt", "r") as file:
        for line in file:
            rows.append(line.split())
    
    total = 0            
    index = 0
    
    # Iterate through stored operators
    for operator in rows[-1]:
        
        temp_total = 0
        
        # Calculate column sum
        if operator == "+":
            for row in range(len(rows) - 1):
                temp_total += int(rows[row][index])
        
        # Calculate column product
        elif operator == "*":
            temp_total = 1
            
            for row in range(len(rows) - 1):
                temp_total *= int(rows[row][index])
        
        # Add column total to problem total
        total += temp_total
        index += 1

    print(total)
    
def vertical_column_layout():
    
    lines = []
    
    with open("day-06-input.txt", "r") as file:    
        for line in file:
            lines.append(line.strip("\n"))
            
    total       = 0
    current_num = 0
    num_list    = []
    calculate_sum     = False
    calculate_product = False
    
    # Iterate through all lines from the end
    for column in range(len(lines[0]) - 1, -1, -1):

        # Iterate through each line in a column
        for row in range(len(lines)):

            current = lines[row][column]

            if current == " ":
                continue

            if current == "+":
                calculate_sum = True
            elif current == "*":
                calculate_product = True
            else:
                current_num *= 10
                current_num += int(current)

        # Store column number if non-zero
        if current_num != 0:
            num_list.append(current_num)
            current_num = 0
        
        temp_total  = 0    
        
        # Calculate group sum
        if calculate_sum:
            for num in num_list:
                temp_total += num

            calculate_sum = False
            num_list      = []

        # Calculate group product
        elif calculate_product:
            temp_total = 1
            for num in num_list:
                temp_total *= num
                
            calculate_product = False
            num_list          = []
        
        # Add temp_total to total
        total += temp_total
                
    print(total)

solve_math_homework()

vertical_column_layout()