lock = [x for x in range(0,100)]
curr = 50 
password = 0

# watch cases where number cross 100, and 0 

with open("input.txt", 'r') as f: 
    data = f.readline()
    
    
    while data: 
        movement = int(data[1::])
        sign = data[0]

        if movement > 99: 
            movement = movement % 100
        if sign == "L":
            curr -= movement
            
        elif sign == "R":
            curr += movement

        if curr > 99: 
            curr = curr % 100
        
        if curr < 0: 
            curr = 100 - (curr * -1)

       
        print("dial is rotated",data, "to point at", curr )

        if curr == 0:
            password += 1
        
        data = f.readline()
print("\nThe password is:",password)

