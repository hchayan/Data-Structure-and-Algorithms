
x,y,z = sorted(list(map(int,input().split())))

while x!=0 or y!=0 or z!=0:
    if x**2+y**2 == z**2:
        print("right")
    else:
        print("wrong")

    x, y, z = sorted(list(map(int, input().split())))