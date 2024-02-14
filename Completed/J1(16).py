score = 0
for i in range(6):
    wins = int(input())
    if wins == 'W':
        score += 1
if score == 5 or score == 6:
    print('1')
elif score == 3 or score == 4:
    print('2')
elif score == 1 or score == 2:
    print('3')
else:
    print('-1')