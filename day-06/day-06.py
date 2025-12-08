
def solve_math_homework():
    
    rows  = []
    total = 0
    
    with open("day-06-input.txt", "r") as file:
        
        for line in file:
            current_row = line.split()
            rows.append(current_row)
            
    index = 0
    
    for operator in rows[-1]:
        
        temp_total = 0
        
        if operator == "*":
            temp_total = 1
            
            for row in range(len(rows) - 1):
                temp_total *= int(rows[row][index])
            
        elif operator == "+":
            
            for row in range(len(rows) - 1):
                temp_total += int(rows[row][index])
        
        total += temp_total
        index += 1

    print(total)

solve_math_homework()