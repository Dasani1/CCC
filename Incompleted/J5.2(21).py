M = int(input())
N = int(input())
K = int(input())

R = []
C = []
for l in range(K):
    rows_and_columns = input()
    if rows_and_columns[0] == "R":
        if rows_and_columns in R:
            R.remove(rows_and_columns)
        else:
            R.append(rows_and_columns)
    elif rows_and_columns[0] == "C":
        if rows_and_columns in C:
            C.remove(rows_and_columns)
        else:
            C.append(rows_and_columns)

r_gold = len(R) 
c_gold = len(C)
print(r_gold)
print(c_gold)
gold = (r_gold*N)+(c_gold*M) - (2 * (r_gold*c_gold))
print(gold)