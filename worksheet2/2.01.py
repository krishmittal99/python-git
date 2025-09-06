# 1. Operations on list L
L = [11, 12, 13, 14]

# (i) Add 50 and 60
L.extend([50, 60])
print("After adding:", L)

# (ii) Remove 11 and 13
L.remove(11)
L.remove(13)
print("After removing:", L)

# (iii) Sort ascending
print("Ascending:", sorted(L))

# (iv) Sort descending
print("Descending:", sorted(L, reverse=True))

# (v) Search for 13
print("13 in L?", 13 in L)

# (vi) Count elements
print("Count:", len(L))

# (vii) Sum all elements
print("Sum:", sum(L))

# (viii) Sum odd numbers
print("Sum of odd:", sum(x for x in L if x % 2 != 0))

# (ix) Sum even numbers
print("Sum of even:", sum(x for x in L if x % 2 == 0))

# (x) Sum prime numbers
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print("Sum of primes:", sum(x for x in L if is_prime(x)))

# (xi) Clear all
L.clear()
print("Cleared:", L)

# (xii) Delete L
del L
