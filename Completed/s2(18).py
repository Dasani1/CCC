num = int(input())
arr = [list(map(int, input().split())) for i in range(num)]

def rotate(arr):
    arr2 = [[0]*num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            arr2[i][j] = arr[num-1-j][i]
    return arr2

def check(arr):
    for row in arr:
        for i in range(1, num):
            if row[i] <= row[i-1]:
                return False
    for row in range(1,num):
        if arr[row][0] <=  arr[row-1][0]:
            return False
    return True

while not check(arr):
    arr = rotate(arr)

for row in arr:
    print(*row)
