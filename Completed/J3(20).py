loops = int(input())
x_coords = []
y_coords = []
for i in range(loops):
    coords = input().split(",")
    x_coords.append(int(coords[0]))
    y_coords.append(int(coords[1]))
minimum_x = min(x_coords)
maximum_x = max(x_coords)
minimum_y = min(y_coords)
maximum_y = max(y_coords)

print(minimum_x-1, minimum_y-1,sep=",")
print(maximum_x+1,maximum_y+1,sep=",")