def find_invalid_ids():
    
    invalid_codes = 0
    
    # Open the file for reading
    with open("test.txt", "r") as file:
        
        # Separate the ranges, delimiting by ','
        data   = file.readline()
        ranges = data.split(',')
        
        # Iterate through each range, assigning upper and lower bounds
        for range_str in ranges:
            bounds      = range_str.split('-')
            lower_bound = int(bounds[0])
            upper_bound = int(bounds[1])
            
            # Validate each number in the range, inclusive
            for num in range(lower_bound, upper_bound + 1):
                num_str = str(num)
                
                if is_invalid_num(num_str):
                    invalid_codes += num
                        
    print(invalid_codes)

def is_invalid_num(input_str):
    midpoint = len(input_str) // 2
    length   = len(input_str)
    
    # Check all potential matching brackets (first char, first 2 chars, ... first half)
    for bracket in range(1, midpoint + 1):
        pattern       = input_str[0:bracket]
        index_tracker = 0
        is_invalid    = True
        
        # Check pattern against segments of input string
        while index_tracker < length:
            segment = input_str[index_tracker:index_tracker + bracket]
            
            # Pattern doesn't match segment, current bracket is valid
            if pattern != segment:
                is_invalid = False
                break
            
            index_tracker += bracket
        
        # Pattern matched all bracket segments
        if is_invalid:
            return True
        
    return False
    
find_invalid_ids()
