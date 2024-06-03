ask = input()
list = ask.lower()
palindromes = []
for j in range(len(list)):
    for i in range(len(list)):
        A2 = list[i:j + 1]
        if A2 == A2[::-1]:
            palindromes.append(len(A2))
print(max(palindromes))

