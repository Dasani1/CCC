distance = list(map(int,input().split()))  
l =[[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(i+1,5):
        l[i][j] = l[i][j-1] + distance[j-1]
    for j in range(i-1,-1,-1):
        l[i][j] = l[i][j+1] + distance[j]

for item in l:
    print(*item)
        
for i in range(5):
    for j in range(i+1,5):
        l[i][j] = l[i][j-1] + distance[j-1]
        l[j][i] = l[i][j]

for item in l:
    print(*item)