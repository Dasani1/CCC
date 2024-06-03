ask = int(input())
list = []
for i in range(ask):
    explosions = int(input())
    list.append(explosions)

too_high = max(list)
list.remove(too_high)
average = 0
for i in range(len(list)):
    average += list[i]

final = average/len(list)
print(final)
