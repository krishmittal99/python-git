p = float(input("Enter principal amount: "))
r = float(input("Enter annual rate (%): "))
t = float(input("Enter time (in years): "))
ci = p * (pow((1 + r/100), t)) - p
print("Compound Interest:", ci)
