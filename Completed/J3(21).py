same = True
def check(ask):
    if (ask[0]+ask[1]) % 2 == 0:
        return True
    
for i in range(4):
    ask = list(map(int,input()))
    

    if (ask[0]+ask[1]) % 2 == 0:
        print("right", end=" ")
        print(ask[2],ask[3],ask[4],end="")
        same = True
    elif (ask[0]+ask[1]) % 2 == 1:
        print("left", end=" ")
        print(ask[2],ask[3],ask[4])
        same = False

    
        
    # if ask == 00000:
    #     print("",end="")
    


