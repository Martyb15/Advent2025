total = 0
def find_max(b: str) -> int:
    left  = int(b[0])
    right = 0
    next  = 1

    # Right battery
    for i, num in enumerate(b):
        if i == len(b)-1:
            continue

        if int(num) > left: 
            left = int(num)
            next = i + 1


    # print("at--", next-1, "left is:", left, end="")

    # Left battery
    for x in range(next, len(b)):
        if int(b[x]) > right: 
            right = int(b[x])

    # print(" at--", n,"right is:", right, end=" -- ")


    # print((left * 10) + right)
    return (left * 10) + right




t= None
with open("input.txt", "r") as f: 
    data = f.readlines()
    for b in data:
  
        b=b.strip()
        

        total += find_max(b)

print(total)
    