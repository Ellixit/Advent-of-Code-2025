
def find_fresh_ingredients():
    
    with open("day-05-input.txt", "r") as file:
        
        lines = [line.strip() for line in file.readlines()]
        
        ranges      = []
        
        for line in lines:
            if line == "":
                break
            line_parts = line.split("-")
            ranges.append((int(line_parts[0]), int(line_parts[1])))
            
        ranges = merge_ranges(ranges)

        fresh_ingredients = count_ranges(ranges)

    return fresh_ingredients

def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    
    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def count_ranges(ranges):
    total = 0
    
    for range_tuple in ranges:
        total += range_tuple[1] - range_tuple[0] + 1
        
    return total

print(find_fresh_ingredients())
