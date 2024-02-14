n = int(input()) # page number
# handle input
d = {}
for i in range(1, n+1):
    m = list(map(int,input().split()))
    d[i] = m[1:]


viewed = []
frontier = [1]
level = 1
shortcut = []
while frontier:
    for i in range(len(frontier)):
        if frontier == d and d == []:
            shortcut.append(d)
        l = frontier.pop(0)
        viewed.append(l)
        for page in d[l]:
            if page not in viewed:
                frontier.append(page)
    level += 1

if len(viewed) == n:
    print("Y")
    print(shortcut[0])
else:
    print("N")