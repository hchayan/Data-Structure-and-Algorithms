skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
import re

def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)

    for i in skill_trees:
        tmp = []
        for ii in i:
            if ii in skill:
                tmp.append(ii)
        print(tmp)
        for i in range(1,len(skill)):
            print(skill, tmp[:i])
            if skill == tmp[:i]:
                answer+=1
        print(answer)
        print("---")




    return answer



print(solution(skill, skill_trees))