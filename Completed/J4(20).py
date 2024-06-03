words = (input())
shifts = input()

def cyclic(shifts):
    shifts = list(shifts)
    previous = shifts.pop(0)
    shifts.append(previous)
    shifts = "".join(shifts)
    return shifts

nah = 0
for j in range(len(shifts)):
    for i in range(len(words)):
        if words[i:len(shifts)+i] == shifts:
            print("yes")
            nah += 1
            break
    if nah == 0:
        shifts = cyclic(shifts)
        print("Checked")
    else:
        break
    
if nah == 0:
    print("no")

        
