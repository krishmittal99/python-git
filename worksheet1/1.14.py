import math as m
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")