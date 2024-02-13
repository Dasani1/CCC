# tune = str(input())
# alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
# numbers = ["1",'2','3','4','5','6','7','8','9','0']
# for i in tune:
#     for j in range(20):
#         if i == alphabet[j]:
#             print(i, end='')
#     for k in tune:
#         if k == '+':
#             print('tighten', end='')
#         elif k == '-':
#             print('loosen', end='')
#     for l in range(10):
#         if i == numbers[l]:
#             print(l+1)

tune = list(input())
number_tracker = False
for i in tune:
    if i.isnumeric():
        number_tracker = True
        print(i,end="")
    elif i.isalpha():
        if number_tracker:
            print()
            number_tracker = False
        print(i,end="")
        number_tracker = ""
    elif i == "+":
        print(" tighten ",end="")
    elif i == "-":
        print(" loosen ",end="")

        
#Almost
