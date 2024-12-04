ask = input()
list = ask.lower()
palindromes = []
for j in range(len(list)):
    for i in range(len(list)):
        # print(list[j:i+1])
        print(list[i-1:j:-1])
        # print(list[len(list)+i:j:-1]+list[i])
#     if list[i:len(list)+i] == list[len(list)+i:i:-1]+list[i]:
#         palindromes.append(len(list[j:i+1]))

# print(max(palindromes))