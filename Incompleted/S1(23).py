c = int(input())
columns = [0]*c
columns_2 = [0]*c
print(columns)
print(columns_2)
first = input()
second = input()
for i in first:
    if i == '1':
        columns[i] += 1
for i in second:
    if i == '1':
        columns_2[i] += 1
print(columns)
print(columns_2)