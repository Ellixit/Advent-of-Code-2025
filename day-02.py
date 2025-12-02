def find_invalid_ids():
    
    invalid_codes = 0
    
    # Open the file for reading
    with open("day-02-input.txt", "r") as file:
        
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
                curr_num = str(num)
                
                # Only numbers of even length can be invalid
                if (len(curr_num) % 2) == 0:
                    
                    # Split first and second half, check if they match
                    midpoint    = len(curr_num) // 2
                    first_half  = curr_num[:midpoint]
                    second_half = curr_num[midpoint:]
                    
                    if first_half == second_half:
                        invalid_codes += num
                        
    print(invalid_codes)
    
find_invalid_ids()
