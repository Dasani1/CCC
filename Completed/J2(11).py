humidity = int(input())
maximum = int(input())
a = 1
t = 1
for i in range(maximum):
    t += 1
    equation = (-6*t**4)+(humidity*t**3)+(2*t**2)+t
    if t >= maximum:
        print("The balloon does not touch ground in the given time.")
        break
    elif equation <= 0:
        print("The balloon first touches ground at hour:")
        print(t)
        break
