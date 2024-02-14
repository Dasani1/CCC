row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
row_4 = input().split()
rows_1 = []
rows_2 = []
rows_3 = []
rows_4 = []
tally = 0
for i in range(4):
    rows_1.append(int(row_1[i]))
    rows_2.append(int(row_2[i]))
    rows_3.append(int(row_3[i]))
    rows_4.append(int(row_4[i]))
for j in range(4):
    if rows_1[j] + rows_2[j] + rows_3[j] + rows_4[j] == sum(rows_1) and sum(rows_2) and sum(rows_3) and sum(rows_4):
        tally += 1
    if sum(rows_1) == sum(rows_2) and sum(rows_2) == sum(rows_3) and sum(rows_3) == sum(rows_4):
        tally += 1
if tally == 8:
    print('magic')
else:
    print('not magic')
print(tally)
# print(rows_1)
# print(rows_2)
# print(rows_3)
# print(rows_4)