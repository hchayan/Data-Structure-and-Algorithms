# [heap]

**: 파이썬 힙 - heapq 모듈**

: 이진 트리 기반의 최소 힙 자료구조. (자바의 PriorityQueue)

: **가지고 있는 요소를 push, pop 할때마다 자동으로 힙 정렬해주는 것**

: nlog(n) 방식으로 정렬 비용 들던거 감소해서 효율.

```python
import heapq

# 힙에 원소 추가
heapq.heappush(원소를 추가할 대상 리스트, 추가할 원소)

# 힙에 원소 삭제
heapq.heappop(리스트)

# 최솟값 삭제하지 않고 얻기
print(리스트[0])

# 기존 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

# ex)
heap = []
heapq.heapphsh(heap, 4)
heapq.heapphsh(heap, 1)
heapq.heapphsh(heap, 7)
heapq.heapphsh(heap, 3)
print(heap)  # [1, 3, 7, 4]
```

<br>

#### [힙 문제 예제]

----

| 번호 |    사이트    |                             문제                             |                    코드                     | 난이도 |        비고         |
| :--: | :----------: | :----------------------------------------------------------: | :-----------------------------------------: | :----: | :-----------------: |
|  1   | 프로그래머즈 | [더 맵게](https://programmers.co.kr/learn/courses/30/lessons/42626#) | [python3](../Quizes/programmers/더 맵게.py) |  lv2   | heaq 모듈 기본 사용 |
|  2   |              |                                                              |                                             |        |                     |