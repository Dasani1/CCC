first = input().split()
N = int(first[0])
RA = float(first[1])
RB = float(first[2])
K = int(first[3])
score = input()
for i in score:
    if i == 'T':
        print(RA, RB)
    elif i == 'W':
        expected = 1/(10**((RB-RA/400)+1))
        new = RA + ((1-expected) * K)
        new -= RA
        new -= RB
        print(RA,RB)
    elif i == 'L':
        expected = 1/(10**(RB-RA/400)) +1
        new = RA + ((0-expected) * K)
        new -= RB
        new += RA
        print(RA,RB)
