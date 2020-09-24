
while True:
    n = input('묵 찌 빠 중 하나를 내주세요. 종료하시려면 엔터를 눌려주세요 : ')
    if n == '':
        break
    elif n in ['묵', '찌', '빠']:
        print(n+"을 내셨습니다")
    else:
        print("묵 찌 빠로 입력하세요")

print("종료합니다")