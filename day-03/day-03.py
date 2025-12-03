

def calculate_highest_joltage():
    
    total = 0
    
    with open("day-03-input.txt", "r") as file:
        
        for line in file:
            
            line = line.strip()
            
            length = len(line)

            total_joltage = "" 
            current       = "0"     # Highest value in window
            curr_index    = 0       # Index of current number to add
            last_index    = 0       # Index of last added number
            
            code_length = 12
            
            for idx in range(code_length):
                
                # Set bounds and establish sliding window
                left_bound      = last_index
                right_bound     = length - (code_length - idx - 1)
                working_segment = line[left_bound:right_bound]
                
                # Find highest value in sliding window
                current    = max(working_segment)
                curr_index = working_segment.find(current)
                    
                # Add current to total, store index of current
                total_joltage += current
                last_index    += curr_index + 1

            total += int(total_joltage)
    
    return total
    
print(calculate_highest_joltage())
