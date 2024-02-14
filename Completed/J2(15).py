emotion = input()
happy = 0
sad = 0
for i in range(len(emotion)):
    if emotion[i:(i+3)] == ":-)":
        happy += 1
    elif emotion[i:(i+3)] == ":-(":
        sad += 1
if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print("happy")
elif happy == sad:
    print('unsure')
else:
    print('sad')