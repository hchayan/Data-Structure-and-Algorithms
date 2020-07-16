import itertools

def nonDivisibleSubset(k, s):
    for i in range(len(s), 0, -1):
        print(i)
        if i == 1:
            return 1
        tmp_list = list(map(','.join, itertools.combinations(s, i)))
        print(tmp_list)



print(nonDivisibleSubset(3, ["1", "7", "2", "4"]))