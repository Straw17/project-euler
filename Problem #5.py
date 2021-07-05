from math import gcd
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lcm = list1[0]
for i in list1[1:]:
    lcm = int(lcm*i/gcd(lcm, i))
print(lcm)
