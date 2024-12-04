triangles = int(input())

triangle1 = list(map(int, input().split()))
triangle2 = list(map(int,input().split()))
counter = 0
border = 0
for i in range(triangles):
    if triangle1[i] == 1:
        if triangle1[i-1] == 1 and i != 0:
            counter += 1
        elif triangle1[i-1] != 1 and i!= 0:
            border = counter + 2
            counter = 0
        border = counter + 2
    elif triangle2[i] == 1:
        if triangle2[i-1] == 1 and i != 0:
            counter += 1
        elif triangle2[i-1] != 1 and i!= 0:
            border = counter + 2
            counter = 0
        border = counter + 2

print(border)