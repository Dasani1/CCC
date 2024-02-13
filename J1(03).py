ast = "*"
white = " "
t = int(input())
s = int(input())
h = int(input())
whole = (s*2)+3
half = (whole//2)
for i in range(t):
    print(ast,(white*s),ast,(white*s),ast,sep='')
print(whole*ast)
for j in range(h):
    print(white*half,ast,sep='')