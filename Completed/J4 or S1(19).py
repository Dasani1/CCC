command = list(input())

a = [1,2]
list_2 = [3,4]

for i in range(len(command)):
    if command[i] == "V":
        a[0:2] = a[2::-1]
        list_2[0:2] = list_2[2::-1]
    elif command[i] == "H":
        a, list_2 = list_2, a
        
print(*a,sep=" ")
print(*list_2,sep=" ")

