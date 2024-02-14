ask = int(input())
good = [0]*5
for _ in range(ask):
    days = input()
    for i in range(5):
        if days[i] == "Y":
            good[i] += 1
best = max(good)
better = []
for i in range(5):
    if good[i] == best:
        better.append(i+1)

better = list(map(str,better))
print(*better,sep=",")

        
    
