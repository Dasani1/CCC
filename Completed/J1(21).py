B = int(input())
pressure = (5 * B) - 400
if pressure > 100:
    print(pressure)
    print(-1)
elif pressure == 100:
    print(pressure)
    print(0)
elif pressure < 100:
    print(pressure)
    print(1)