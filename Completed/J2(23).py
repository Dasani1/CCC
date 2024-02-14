ask = int(input())
scoville = 0
for i in range(ask):
    peppers = input()
    if peppers == "Poblano":
        scoville += 1500
    elif peppers == "Mirasol":
        scoville += 6000
    elif peppers == "Serrano":
        scoville += 15500
    elif peppers == "Cayenne":
        scoville += 40000
    elif peppers == "Thai":
        scoville += 75000
    elif peppers == "Habanero":
        scoville += 125000
print(scoville)