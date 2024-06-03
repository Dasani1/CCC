rb_side_times = list(map(int,input().split()))

robot = rb_side_times[0]
side = rb_side_times[1]
times = rb_side_times[2]
robots = list(map(int,input().split()))
left = [0,1]
right = [-1,-2]
for i in range(times):
    if robots[left[0]] + robots[left[1]] >= robots[right[0]] + robots[right[1]]:
        print(robots[left[0]] + robots[left[1]])
    else:
        print(robots[right[0]] + robots[right[1]])  

