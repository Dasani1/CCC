tune = list(input())

nums = ["1","2","3","4","5","6","7","8","9","0"]

for i in range(len(tune)):
    if tune[i] not in nums and (tune[i] != "-" and tune[i] != "+"):
        print(tune[i], end="")
    elif tune[i] == "+" or tune[i] == "-":
        if tune[i] == "+":
            print(" tightens ", end = "")
        else:
            print(" loosens ", end = "")
    elif tune[i] in nums:
        print(tune[i], end = "")

#13 points