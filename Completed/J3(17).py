coords = list(map(int,input().split()))
coords2 = list(map(int, input().split()))
possible = int(input())

x_diff = abs(coords[0] - coords2[0])
y_diff = abs(coords[1] - coords2[1])
total = x_diff + y_diff
odd_or_even = True
if total % 2 == 0:
    odd_or_even = True 
else:
    odd_or_even = False
if possible < total:
    print("N")
elif odd_or_even == False and possible % 2 == 1 or odd_or_even and possible % 2 == 0:
    print("Y")
else:
    print("N")

