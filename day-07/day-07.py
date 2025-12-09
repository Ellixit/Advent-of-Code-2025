
def calculate_beam_split():
    
    rows = []
    
    with open("day-07-input.txt", "r") as file:
        rows = [list(row.rstrip("\n")) for row in file]
        
    last_row = len(rows)
    
    start_index = rows[0].index("S")
    
    beam_indices = {start_index}
    splits       = 0
    
    # Iterate through each row
    for idx in range(1, last_row):
        
        # Iterate through each column
        for column in range(0, len(rows[0])):
        
            current = rows[idx][column]

            # Split beam on splitter
            if current == "^" and column in beam_indices:
                beam_indices.remove(column)
                splits += 1
                
                # Create left beam if in bounds
                if column - 1 >= 0:
                    beam_indices.add(column - 1)
                    rows[idx][column - 1] = "|"
                
                # Create right beam if in bounds
                if column + 1 < len(rows[0]):
                    beam_indices.add(column + 1)
                    rows[idx][column + 1] = "|"
                    
            # Just useful for debugging
            elif column in beam_indices:
                rows[idx][column] = "|"
                
        print("".join(rows[idx]))
        
    print(splits)


def find_timelines():

    with open("day-07-input.txt", "r") as file:
        rows = [list(row.rstrip("\n")) for row in file]

    start_index = rows[0].index("S")
    memo = {}

    timelines = find_timelines_helper(1, start_index, rows, memo)
    print(timelines)


def find_timelines_helper(row_idx, beam_idx, rows, memo):
    
    # Beam out of bounds
    if beam_idx < 0 or beam_idx >= len(rows[0]):
        return 0

    # Reached bottom of graph
    if row_idx == len(rows):
        return 1

    # Check memo for previously calculated path
    key = (row_idx, beam_idx)
    if key in memo:
        return memo[key]

    if rows[row_idx][beam_idx] == "^":
        val = (
            find_timelines_helper(row_idx+1, beam_idx-1, rows, memo) +
            find_timelines_helper(row_idx+1, beam_idx+1, rows, memo)
        )
    else:
        val = find_timelines_helper(row_idx+1, beam_idx, rows, memo)

    memo[key] = val
    return val

find_timelines()
