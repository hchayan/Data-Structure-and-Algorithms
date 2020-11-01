def solution(phone_book):
    lis = []
    for phone in phone_book:
        for num in lis:
            tmp = min(len(num), len(phone))
            if phone[:tmp] == num[:tmp]:
                return False
        lis.append(phone)
    return True

print(solution(["123", "456", "789"]))