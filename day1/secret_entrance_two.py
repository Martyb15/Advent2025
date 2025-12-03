curr = 50 
password = 0

# watch cases where number cross 100, and 0 

with open("input.txt", 'r') as f: 
    data = f.readline()
    
    
    while data: 
        movement = int(data[1::])
        sign = data[0]

        # break down movements over 99
        if movement > 99: 
            password += movement // 100
            movement = movement % 100


        # check direction
        if sign == "L":
            if (curr - movement) <= 0 and curr > 0: 
                password += 1
            curr -= movement  
        elif sign == "R":
            if (curr + movement) > 99: 
                password += 1
            curr += movement

        # ensure location pointed at is in range
        if curr > 99: 
            curr = curr % 100
        
        if curr < 0: 
            curr = 100 - (curr * -1)

       
        print("dial is rotated",data, "to point at", curr )

 
        
        data = f.readline()
print("\nThe password is:",password)


