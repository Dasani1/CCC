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
    rem = len(frontier)
    for i in range(len(frontier)):
        if d[frontier[i]] == []:
            shortcut.append(level)
        l = frontier[i]
        viewed.append(l)
        for page in d[l]:
            if page not in viewed:
                frontier.append(page)
    level += 1
    del frontier[:rem]

if len(set(viewed)) == n:
    print("Y")
    print(shortcut[0])
else:
    print("N")