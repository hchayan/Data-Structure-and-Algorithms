def migratoryBirds(arr):
    birds = [0, 0, 0, 0, 0]
    for a in arr:
        birds[a-1] += 1

    maxx = max(birds)

    for i in range(5):
        if maxx == birds[i]:
            return i+1

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
print(migratoryBirds([1,1,2,2,3]))