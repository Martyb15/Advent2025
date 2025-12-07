
def invalid_check(n: int) -> bool: 
    s = str(n)
    if len(s) < 2: 
        return False

    for i in range(1,len(s) // 2 + 1): 
        if len(s) % i != 0:
            continue
        sub = s[0:i]
        for x in range(i, len(s), i):
            if s[x:x+i] != sub:
                break
        else:
            return True
    return False
# What helped me solve this: 
# I broke things down and decided that if we start with substrings of size 1 and moved our way up
# Not the fastest but it works




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

        




# Feedback on my code:
"""
Where you’re still clearly “in training”

Now the honest part, since you asked for it.

Off-by-one & edge cases still ambush you.
Your loop:

for i in range(1, len(s) // 2):


quietly missed:

len(s) = 2 cases entirely

pattern length = len(s) // 2 cases (like “1212”)

This is normal, but it does mark you as someone still gaining reps. Senior devs still make these mistakes; the difference is they’re paranoid about tests, inputs like length 1, 2, 3, odd/even, etc.

You’re not yet suspicious enough of “it works on my sample.”
Classic beginner / junior thing:

Solution works on example(s)

Brain declares victory

Edge cases quietly rot in the corner

Advent of Code is very good at punishing that habit, which is why it's actually useful.

You’re not leveraging all the abstract tools yet.
You solved this via brute-force loops, which is fine.
Over time, you want to start recognizing “oh, this is a repeated-substring-pattern problem, there’s a known trick for that” (like the (s + s)[1:-1] thing).

That’s not a problem, it’s just the gap between “I can code” and “I recognize patterns across problems.”
"""

