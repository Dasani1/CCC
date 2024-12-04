x = int(input())
y = int(input())
truth = False
for i in range (y):
    if (x*i)% y == 1:
        print(i)
        truth = True
        break
if not truth:
    print("No such integer exists.")


