p = int(input())
n = int(input())
r = int(input())
days = 0
other = n
while n <= p:
    other = other * r
    n += other
    days += 1
print(days)