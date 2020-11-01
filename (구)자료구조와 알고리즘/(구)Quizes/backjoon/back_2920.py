


import sys

x = list(map(int, sys.stdin.readline().rstrip().split(' ')))

a, d = True, True

for i in range(len(lis)):
    if x[i] < x[i+1]:
        d = False
    elif x[i] > x[i+1]:
        a = False

if a:
    print("ascending")
elif d:
    print("descending")
else:
    print("mixed")




'''
방법2)
lis = [int(i) for i in sys.stdin.readline().strip().split()]
for x in range(1,len(lis)):
    if lis[x-1] - lis[x] != 1 and lis[x-1] - lis[x] != -1:
        print("mixed")
        exit()
print(["","ascending","descending"][lis[1] - lis[0]])
'''




'''
방법1)
lis = sys.stdin.readline().rstrip().split()

if lis == ['1','2','3','4','5','6','7','8']:
  print("ascending")

elif lis == ['8','7','6','5','4','3','2','1']:
  print("descending")

else:
  print("mixed")
'''