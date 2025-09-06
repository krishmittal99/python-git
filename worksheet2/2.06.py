S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i)
S1.update([55, 66])
print(S1)

# (ii)
S1.discard(10)
S1.discard(30)
print(S1)

# (iii)
print("40 in S1?", 40 in S1)

# (iv)
print("Union:", S1 | S2)

# (v)
print("Intersection:", S1 & S2)

# (vi)
print("S1 - S2:", S1 - S2)
