

for nn in range(int(input())):
    P,Q,R,S,W = map(int, input().split())
    com_A = P * W
    com_B = Q
    if R < W:
        com_B += (W-R) * S
    print("#"+str(nn+1)+" "+str(com_A if com_A < com_B else com_B))