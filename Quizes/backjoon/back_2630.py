
paper = []
count = 0

def countPaper(info_list):
    global count
    if len(info_list) == 1:
        if info_list[0][0] == 1:
            return 1
        else:
            return 0

    mid = len(info_list)
    now = countPaper(info_list[:mid][:mid]) + countPaper(info_list[mid:][:mid]) + countPaper(info_list[:mid][mid:]) + countPaper(info_list[mid:][mid:])
    if now == 0:
        return 0
    elif now > 0 and now < 4:
        count += now
        return 0
    else:
        return 1


for i in range(int(input())):
    paper.append(list(map(int,input().split())))


print(countPaper(paper))