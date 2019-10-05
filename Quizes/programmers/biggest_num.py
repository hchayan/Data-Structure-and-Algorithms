import itertools

def solution(numbers):

    numbers = list(map(str, numbers))
    tmp = []
    numbers.sort(reverse=True)


    print(numbers)



print(solution([335,330,33,5,9]))