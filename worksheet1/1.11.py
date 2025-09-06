import math as m
x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter second point (x2 y2): ").split())
dist = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean Distance:", dist)
