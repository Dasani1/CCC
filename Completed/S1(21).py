ask = int(input())
area = 0
height = list(map(int,input().split()))
base = list(map(int,input().split()))

for i in range(ask):
    area += (base[i] * ((height[i] + height[i+1])/2))

print(area)