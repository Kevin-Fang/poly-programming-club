import math
n_primes = []

max_val = 100
for i in range(2, max_val):
    n_primes.append(True)

p = 2
for i in range(2, math.ceil(math.sqrt(max_val))):
    if n_primes[i]:
        num_multiples = (max_val - (i ** 2)) // i
        for j in range(num_multiples):
            dividing_val = i ** 2 + j * i
            n_primes[j] = False

for i, x in enumerate(n_primes):
    if x:
        print(i)
