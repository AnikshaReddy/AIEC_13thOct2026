def temperature_fuzzy(temp):
    if temp <= 20:
        cold = 1
    elif temp < 30:
        cold = (30 - temp) / 10
    else:
        cold = 0

    if temp <= 20 or temp >= 40:
        warm = 0
    elif temp < 30:
        warm = (temp - 20) / 10
    else:
        warm = (40 - temp) / 10

    if temp <= 30:
        hot = 0
    elif temp < 40:
        hot = (temp - 30) / 10
    else:
        hot = 1

    if cold >= warm and cold >= hot:
        speed = "Low"
    elif warm >= hot:
        speed = "Medium"
    else:
        speed = "High"

    print("Temperature:", temp)
    print("Cold membership:", round(cold, 2))
    print("Warm membership:", round(warm, 2))
    print("Hot membership:", round(hot, 2))
    print("Fan speed:", speed)

temp = float(input("Enter temperature: "))
temperature_fuzzy(temp)