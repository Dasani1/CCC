players = int(input())
gold = 0
for i in range(players):
    scored = int(input())
    fouls = int(input())
    if (scored*5) - (fouls*3) > 40:
        gold += 1
if gold == players:
    print(str(gold) + "+")
else:
    print(gold)
    