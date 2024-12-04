ask = int(input())
days = []
available = [0,0,0,0,0]
for i in range(ask):
    avail = list(input())
    days.append(avail)

for i in range(ask):
    for j in range(5):
        if days[i][j] == "Y":
            available[j] += 1
big = max(available)
true = []

for i in range(5):
    if available[i] == big:
        true.append(i+1)
        
print(*true, sep=",")
