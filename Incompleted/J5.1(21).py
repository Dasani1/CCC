M = int(input())
N = int(input())
K = int(input())

commands = []
command_counter = []    
true_commands = []
for l in range(K):
    rows_and_columns = input()
    if rows_and_columns in commands:
        commands.remove(rows_and_columns)
    else:
        commands.append(rows_and_columns)
rows_gold = 0
columns_gold = 0
row_counter = 0
column_counter = 0
for i in range(len(commands)):
    if commands[i][0] == "R":
        row_counter += 1
        rows_gold += 1
    elif commands[i][0] == "C":
        column_counter += 1
        columns_gold += 1
intersections = -2*(row_counter*column_counter)
total_gold = (rows_gold*N) + (columns_gold*M)
final = total_gold - abs(intersections)
print(final)
print(intersections)
print(rows_gold, columns_gold)
print(row_counter,column_counter)
print(total_gold)