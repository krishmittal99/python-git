# 4. Count upper/lower
def count_case(s):
    d = {"UPPER":0, "LOWER":0}
    for c in s:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
    return d
