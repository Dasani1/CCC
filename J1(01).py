num = int(input())
ast = "*"
white = " "
star = 1
space = (num*2) - 2
half = (num // 2) 
for i in range(num):    
    if i < half:
        print((star*ast),(space*white),(star*ast),sep='')
        star += 2
        space -= 4
    elif i >= half:
        print((star*ast),(space*white),(star*ast),sep='')
        star -= 2
        space += 4
        