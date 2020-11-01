import sys

lis = []
for nn in range(int(sys.stdin.readline().rstrip())):
    name,a,b,c =  sys.stdin.readline().rstrip().split()
    lis.append([int(a),int(b),int(c),name])

for a,b,c,name in sorted(lis, key= lambda score: (100-score[0], score[1], 100-score[2], score[3])):
    print(name)

