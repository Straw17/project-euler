primes = []
i = 3
while True:
    isPrime = True
    for x in range(2, round(i/2)):
        if i%x == 0:
            isPrime = False
            break
    if isPrime == True:
        primes.append(i)
        if len(primes) == 10001:
            print(i)
    i += 1
