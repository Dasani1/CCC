num = int(input())
l = []
for i in range(num):
    l.append(list(map(int, input().split())))

new_l = [[0 for i in range(num)] for j in range(num)]
two_l = [[0 for i in range(num)] for j in range(num)]
three_l = [[0 for i in range(num)] for j in range(num)]
for i in range(num):
    for j in range(num):
        new_l[i][j] = l[num-1-j][i]
for i in range(num):
    for j in range(num):
        two_l[i][j] = new_l[num-1-j][i]
for i in range(num):
    for j in range(num):
        three_l[i][j] = two_l[num-1-j][i]

for item in l:
    print(*item)
for item in new_l:
    print(item)
for item in two_l:
    print(item)
for item in three_l:
    print(item)


    

