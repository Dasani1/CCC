k = int(input())
word = input()
final_order = []

Sequence = 1
for i in range(len(word)):
    letter = ord(word[i])
    formula = (3*Sequence) + k
    letter = letter - formula
    if letter < 65:
        letter += 26
        final_order.append(chr(letter))
        Sequence += 1
    else:
        final_order.append(chr(letter))
        Sequence += 1
print(*final_order,sep="")