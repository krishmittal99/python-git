# 10. Classify temperature
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"
