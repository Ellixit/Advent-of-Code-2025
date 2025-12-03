

def calculate_highest_joltage():
    
    total = 0
    
    with open("day-03-input.txt", "r") as file:
        
        for line in file:
            
            line = line.strip()
            
            length = len(line)

            joltage_ten = max(line)
            index = line.find(joltage_ten)
            
            if length - 1 == index:
                joltage_ten = max(line[:length - 1])
                index = line.find(joltage_ten)
                
            joltage_one = max(line[index + 1:])
            
            output = f"{joltage_ten}{joltage_one}"
    
            total += int(output)
    
    return total
    
print(calculate_highest_joltage())
