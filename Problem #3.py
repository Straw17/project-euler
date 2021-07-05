i = 1
primeFactors = []
num = 600851475143
while True:
	if i < num and num % i == 0:
		isPrime = True
		for x in range(2, round(i/2)):
			if i%x == 0:
				isPrime = False
				break
		if isPrime:
			primeFactors.append(i)
			print(str(i) + ' is prime.')
	elif i > num:
		break
	i += 1
print('Task complete.)
