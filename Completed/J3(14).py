rounds = int(input())
d_rolls = []
a_rolls = []
david = 100
antonia = 100
for i in range(rounds):
    rolls = list(map(int,input().split()))
    a_rolls.append(rolls[0])
    d_rolls.append(rolls[1])
    if a_rolls[i] == d_rolls[i]:
        pass
    elif a_rolls[i] > d_rolls[i]:
        david -= a_rolls[i]
    elif d_rolls[i] > a_rolls[i]:
        antonia -= d_rolls[i]
print(antonia)
print(david)
