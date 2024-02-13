ask = int(input())
number = []
sign = []
for i in range(ask):
    code = input().split()
    number.append(int(code[0]))
    sign.append(code[1])
    print(number[i]*sign[i])

