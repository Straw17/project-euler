import math, sys

for a in range(1000):
    for b in range(1000):
        c = math.sqrt((a**2)+(b**2))
        if int(c) == c and a < b < c:
            print([a, b, c])
            if a + b + c == 1000:
                print(a*b*c)
                sys.exit()
