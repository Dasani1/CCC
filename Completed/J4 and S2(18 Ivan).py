num = int(input())
l = []
for i in range(num):
    l.append(list(map(int, input().split())))
   
def check(l):
    if l[0][1] <= l[0][0]:
        return False
    if l[1][0] <= l[0][0]:
        return False
    return True

def rotate(l):
    new_l = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        for j in range(num):
            new_l[i][j] = l[num-1-j][i]
    return new_l

while not check(l):
    l = rotate(l)

for item in l:
    print(*item)