bombs_and_height = list(map(int,input().split()))
N = bombs_and_height[0]
D = bombs_and_height[1]
height_of_bombs = list(map(int,input().split()))

bombs_needed = 1
largest_explosion = 1

explosions = []
for i in range(1,N):
    if abs(height_of_bombs[i] - height_of_bombs[i-1]) <= D:
        largest_explosion += 1
        print("Check")
    elif abs(height_of_bombs[i] - height_of_bombs[i-1]) != D:
        bombs_needed += 1
        print("Uncheck")
        explosions.append(largest_explosion)
        largest_explosion = 1
explosions.append(largest_explosion)
print(explosions)
print(bombs_needed)
print(max(explosions))