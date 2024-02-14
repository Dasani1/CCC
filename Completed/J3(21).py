direction = "idk"
for _ in range(4):
    ask = list(map(int,input()))
    if ask[0] == 9 and ask[1] == 9 and ask[2] == 9 and ask[3] == 9:
        pass
    elif ask[0] == 0 and ask[1] == 0:
        print(f"{direction} {ask[2]}{ask[3]}{ask[4]}")

    elif (ask[0]+ask[1]) % 2 == 0:
        print(f"right {ask[2]}{ask[3]}{ask[4]}")
        direction = "right"

    elif (ask[0]+ask[1]) % 2 == 1:
        print(f"left {ask[2]}{ask[3]}{ask[4]}")
        direction = "left"

