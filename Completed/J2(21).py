ask = int(input())
names = []
amounts = []
for _ in range(ask):
    name = input()
    amount = int(input())
    names.append(name)
    amounts.append(amount)

check = amounts.index(max(amounts))
print(f"{names[check]}")


