N = int(input())
K = int(input())
result = 0
for i in range(K+1):
    result += N
    N *= 10
    print(result)
print(result)