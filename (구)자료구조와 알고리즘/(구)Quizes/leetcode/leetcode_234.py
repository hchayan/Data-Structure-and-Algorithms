def isPalindrome(head):
    slow, fast = head, head
    tmp = []
    while fast and fast.next:
        tmp.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    # 요소 홀수 일때 가운데값 패
    if fast:
        slow = slow.next

    while slow and len(tmp) > 0:
        if slow.val != tmp.pop():
            return False
        slow = slow.next

    return True

