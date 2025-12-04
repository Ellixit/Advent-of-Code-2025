def decode_password():
    
    password_count = 0
    lock_position  = 50

    with open("day-01-input.txt", "r") as input_file:
        
        for line in input_file:

            direction  = line[0]
            amount_num = int(line[1:])

            if direction == "L":
                distance = lock_position % 100
            else:
                distance = (100 - lock_position) % 100

            if distance == 0:
                distance = 100

            if amount_num >= distance:
                password_count += 1 + (amount_num - distance) // 100

            if direction == "L":
                lock_position = (lock_position - amount_num) % 100
            else:
                lock_position = (lock_position + amount_num) % 100
            
    print(password_count)

decode_password()
