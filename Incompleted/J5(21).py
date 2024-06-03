M = int(input())
N = int(input())
K = int(input())

grid = [["B" for i in range(N)] for j in range(M)]
d = {}
commands = []
command_counter = []
for l in range(K):
    rows_and_columns = input().split()
    num = int(rows_and_columns[1])
    commands.append(rows_and_columns[0]+rows_and_columns[1])

for a in range(len(commands)):
    check = commands.count(commands[a])
    command_counter.append(check)
print(command_counter)
print(commands)
# valid_commands = []
# invalid_commands = []
# for a in range(len(commands)):
#     first_value = commands[0]
#     if first_value == commands[a]:
#         command_counter += 1
#     if command_counter % 2 == 0:
#         invalid_commands.append(first_value)
#         commands.pop(0)
#         command_counter = 0
#     elif command_counter % 2 == 1:
#         valid_commands.append(first_value)
#         commands.pop(0)
#         command_counter = 0

# print(valid_commands)
# print(invalid_commands)





    # if rows_and_columns[0] == "R":
    #     for i in range(N):
    #         if grid[num-1][i] == "B":
    #             grid[num-1][i] = "G"

    #         elif grid[num-1][i] == "G":
    #             grid[num-1][i] = "B"

    # elif rows_and_columns[0] == "C":
    #     for i in range(M):
    #         if grid[i][num-1] == "B":
    #             grid[i][num-1] = "G"
                
    #         elif grid[i][num-1] == "G":
    #             grid[i][num-1] = "B"
# gold_counter = 0
# for i in range(N):
#     for j in range(M):
#         if grid[i][j] == "G":
#             gold_counter += 1
# print(grid)
# print(gold_counter)

