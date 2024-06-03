p = int(input())
n = int(input())
r = int(input())
days = 0
iteration = 0
other = n
while n <= p:
    n *= r
    other += n
    days += 1
print(days-1)