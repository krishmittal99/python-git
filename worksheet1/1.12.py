a, b, c = map(int, input("Enter three angles separated by space: ").split())
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Valid Triangle")
else:
    print("Not a Triangle")
