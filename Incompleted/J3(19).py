ask = int(input())
length = 0
symbol = 0
for i in range(ask):
    check = list(input())
    check.append("小") #Sabrina
    for j in range(1,len(check)):
        symbol = check[j-1] #Sabrina
        if check[j] == check[j-1]:
            length += 1
        elif check[j] != check[j-1]:
            print(length+1,symbol,end=" ")
            length = 0
    print() #Sabrina
    