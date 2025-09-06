D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i)
D[8] = 8.8
print(D)

# (ii)
D.pop(2)
print(D)

# (iii)
print("6 key present?", 6 in D)

# (iv)
print("Count:", len(D))

# (v)
print("Sum of values:", sum(D.values()))

# (vi)
D[3] = 7.1
print(D)

# (vii)
D.clear()
print("Cleared:", D)
