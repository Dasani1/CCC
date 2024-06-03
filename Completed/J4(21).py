order = list(input())
L = order.count("L")
M = order.count("M")
S = order.count("S")

Non_L = 0
Non_M = 0
duplicates = 0
M_Counter = 0
L_Counter = 0
duplicate_checker = True
for i in range(L):
    if order[i] == "M":
        M_Counter += 1
        Non_L += 1
    elif order[i] == "S":
        Non_L += 1

for i in range(L,L+M):
    if order[i] == "L":
        L_Counter += 1
        Non_M += 1
    elif order[i] == "S":
        Non_M += 1

minimum = [M_Counter, L_Counter]

final = (Non_L + Non_M)-(min(minimum))
#LLLMMSLSSMSSLSMSLSMLSMLSMLSMLSMSLMSLSSSLMSL
#LLLMMSLSSMSS
#LLSLLSLSLSLSLSSS
#This doesn't work
print(final)
print(order[0:L])
print(order[L:])

