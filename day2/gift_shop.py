
def invalid_check(n: int) -> bool: 
    s = str(n)
    if len(s) % 2 != 0: 
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


total = 0


with open("input.txt", "r") as f:

    line = f.readline().strip()
    ranges = line.split(",")

    for r in ranges:
        if not r:            
            continue

        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        for n in range(start, end +1): 
            if invalid_check(n):
                total += n
print(total)
        


