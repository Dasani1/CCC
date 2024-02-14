spaces = int(input())
overlap = 0
yesterday = input()
today = input()

for i in range(spaces):
    if yesterday[i] == "C" and today[i] == "C":
        overlap += 1
print(overlap)
    
