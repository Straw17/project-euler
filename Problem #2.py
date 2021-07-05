evenSum = 2
fib1 = 1
fib2 = 2
nextNum = 3
while nextNum < 4000000:
    if nextNum % 2 == 0:
        evenSum += nextNum
    fib1 = fib2
    fib2 = nextNum
    nextNum = fib1 + fib2
print(evenSum)
