import sys
input = sys.stdin.readline

ask = int(input())

scores = []
scorey = set()
for i in range(ask):
    scores_1 = int(input())
    scores.append(scores_1)
    scorey.add(scores_1)

new = sorted(scorey)
count = scores.count(new[-3])
print(new[-3], count)

