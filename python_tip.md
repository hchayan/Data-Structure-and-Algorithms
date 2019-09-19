# 파이썬 팁

: 파이썬을 이용해 문제를 풀면서 알게된 파이썬 문법 작성 팁입니다.



1. 문자열 뒤집기

   ```python
   x = x[::-1]
   ```

   ------

   

2. **한줄 for문**

   ```python
   # 기본 형태
   [표현식 for 항목 in 순회가능객체]
   
   # 응용 형태
   1) if문 포함형태 : [표현식 for 항목 in 순회가능객체 if 조건문]
   2) 중첩문 형태 : [표현식 for 항목1 in 순회가능객체 for 항목2 in 순회가능객체2]
   3) set형태로 저장 : (표현식 for 항목 in 순회가능객체)
   4) dict형태로 저장 : {표현식 for 항목 in 순회가능객체}
   
   
   # 예시
   print([i for i in [1,2,3]])
   
   ```

   

3. **한줄 if문**

   ```python
   # 기본 형태
   True일때실행문 if 조건식 else False일때실행문
   
   
   #예시
   if x > 5:
       print("big")
   else:
       print("small")
       
   =>
   print("big") if x > 5 else print("small")    
   
   
   #예시2
   if x = "a":
       res += 1
   else:
       res = 0
       
   =>
   res= res+1 if x = "a" else 0
   
   
   '''
   쉽게 생각하면
   
   if 조건문 'true결과' else 'false결과'
   
   처럼 기존의 식 한줄로 쓴뒤,
   'true결과'와 if 조건문의 위치를 변경해 준다고 보면된다.
   '''
   ```

   

4. **lamda 함수(한줄 함수)**

   ```
   # 기본식
   lambda 입력값:출력식
   
   
   # 예시
   1) ans = lambda x:x**2
      print(ans(9))    # 결과 81
      
   2) 독립적인 사용(중요)
   def add(n):
     return lambda x:x+n
     
   a = add(2)
   b = add(4)
   print(a(5))       # 2+5 = 7
   print(add(2)(5))  # 7
   ```

   

5. **list내 요소들 타입 변환(map함수)**

   ```python
   x = list(map(int,리스트변수))              # 리스트내 요소를 정수형(int)으로 변환
   
   #응용 ************
   a = 문자열
   x = sum(map(a.count,[원소1,원소2,원소3]))   #문자열내의 각 원소의 개수를 센뒤 그 값을 더함
   ```

   ------

   

6. 리스트 요소 -> 문자열 변환

   ```python
   x = ' '.join(리스트변수)             # 리스트내 요소를 ' '간격을 둔체 문자열형태로 연결
   ```

   -------



7. collections 모듈

   ```
   리스트내 요소 개수를 구할수 있다.
   
   lst = ['a','b','c','a','b']
   print(collections.Counter(lst))
   
   결과 : Counter({'a':2,'c':1,'b':1})
   ```

   

8. 리스트(int) 내용 출력

   ```
   res = [1, 2, 3, 4]
   print(*res)             # 1, 2, 3, 4 출력
   ```


9.  무한 입력값

   ```
   for x in sys.stdin:
   ```

10.  **최대공약수, 최소공배수**

    ```
    # 최대공약수 : 유클리드 공식을 이용해 구하기
    
    gcd(a,b) => gcd(b,r)   #r = a%b  (a>b일때) 
    이렇게 하다 b%r == 0이되는 r이 최대공약수.
    
    # 최소공배수 : a*b/r
    ```

    

11. 숫자 진법 변환(n진법 -> 10진법)

    ```
    int(n진법 숫자, n)   # n진법 숫자를 10진법 숫자로 변경
    ```

    