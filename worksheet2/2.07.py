import random, string

# helper: prime check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# (i) 100 random strings
print("100 random strings:")
for _ in range(100):
    length = random.randint(6, 8)
    s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    print(s)

# (ii) Primes 600–800
print("\nPrime numbers between 600 and 800:")
for n in range(600, 801):
    if is_prime(n):
        print(n, end=" ")
print()

# (iii) Numbers divisible by 7 and 9 between 100–1000
print("\nNumbers divisible by 7 and 9 between 100–1000:")
for n in range(100, 1001):
    if n % 7 == 0 and n % 9 == 0:
        print(n, end=" ")
print()
