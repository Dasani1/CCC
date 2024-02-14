# ask = input().split()
# ask = list(map(int,ask))

# l = [[0 for i in range(5)] for i in range(5)]

# for i in range(5):
#     for i in range(5):
#         pass
ask = input().split()
i = [0]
for j in range(4):
    i.append(int(ask[j]))

    

print(i[0], i[0]+i[1] ,i[0]+i[1]+i[2], i[0]+i[1]+i[2]+i[3], i[0]+i[1]+i[2]+i[3]+i[4])
print(i[0]+i[1], i[0], i[0]+i[2], i[0]+i[2]+i[3], i[0]+i[2]+i[3]+i[4])
print(i[2]+i[1]+i[0], i[2]+i[0], i[0], i[3], i[3]+i[4]) #i[3]+i[0]? #i[3]+i[4]+i[0]?
print(i[0]+i[3]+i[2]+i[1], i[0]+i[3]+i[2], i[0]+i[3], i[0], i[0]+i[4])
print(i[4]+i[3]+i[2]+i[1]+i[0], i[4]+i[3]+i[2]+i[0], i[4]+i[3]+i[0], i[4]+i[0], i[0])