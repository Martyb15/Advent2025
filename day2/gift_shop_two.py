
def invalid_check(n: int) -> bool: 
    s = str(n)
    if len(s) < 2: 
        return False

    for i in range(1,len(s)): 
        sub = s[0:i]
        for x in range(i, len(s), i):
            if s[x:x+i] != sub:
                break
        else:
            return True
    return False


    
    # for i in range(len(s)):
    #     if i == 0:
    #         continue 
    #     if len(s) % i != 0: 
    #         continue


            

    #     sub = len(s) // i
        
    #     x = s[:sub]
    #     for j in range(sub,len(s), sub):
    #         temp = s[j:j+sub]
    #         if temp != x:
    #             continue   
    #     return True
    # return False



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

        


