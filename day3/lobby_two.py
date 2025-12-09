total = 0



def find_max(b: str) -> int:
    digits = [int(x) for x in b]
    battery = []
    start = 0


    for selected in range(12) :
        remaining = 12 - selected
        end = len(digits) - remaining + 1   
        best = -1
        best_idx = -1

        for i in range(start, end):
            if digits[i] > best:
                best = digits[i]
                best_idx = i
        start = best_idx + 1
        battery.append(best)

    return int(''.join(str(d) for d in battery))




t= None
with open("part2.txt", "r") as f: 
    data = f.readlines()
    for b in data:
  
        b=b.strip()
        

        total += find_max(b)

print(total)
    