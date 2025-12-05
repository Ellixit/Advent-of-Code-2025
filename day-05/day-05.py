
def find_fresh_ingredients():
    
    fresh_ingredients = 0
    
    with open("day-05-input.txt", "r") as file:
        
        lines = [line.strip() for line in file.readlines()]
        
        ranges      = []
        scan_ranges = True
        
        for line in lines:
            
            if line == "":
                scan_ranges = False
                continue
                
            if scan_ranges:
                line_parts = line.split("-")
                ranges.append((int(line_parts[0]), int(line_parts[1])))
            else:
                fresh_ingredients += check_ranges(ranges, int(line))

    return fresh_ingredients

def check_ranges(ranges, number):
    
    for range_tuple in ranges:
        if number > range_tuple[0] and number <= range_tuple[1]:
            return 1
        
    return 0

print(find_fresh_ingredients())