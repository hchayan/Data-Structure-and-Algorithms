import sys
lis = [int(i) for i in sys.stdin.readline().strip().split()]
for x in range(1,len(lis)):
    if lis[x-1] - lis[x] != 1 and lis[x-1] - lis[x] != -1:
        print("mixed")
        exit()
print(["","ascending","descending"][lis[1] - lis[0]])


'''
lis = sys.stdin.readline().rstrip().split()

if lis == ['1','2','3','4','5','6','7','8']:
  print("ascending")

elif lis == ['8','7','6','5','4','3','2','1']:
  print("descending")

else:
  print("mixed")
'''