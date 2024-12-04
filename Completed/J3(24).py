players = int(input())
scores = set()
thirds = []
for i in range(players):
    score = int(input())
    scores.add(score)
    thirds.append(score)
new_scores = sorted(scores)
counter = thirds.count(new_scores[-3])
print(new_scores[-3], counter)

        


    


