import sys

x = int(sys.stdin.readline().rstrip())

for i in range(x):
  temp = sys.stdin.readline().rstrip().split(' ')
  print(int(temp[0])+int(temp[1]))
  
  
  
  '''
  [출력의 시간 절약 ]
  input() 대신 sys.stdin.readline() 을 사용하면 반복문에서 효과적인 시간 절약을 야기한다.
  
  + readlines()로 여러문장 받아오기 가능
  + 해당문 앞 뒤에 int(...), .split() 같은거 바로 사용가능
  + rstrip() : 위 문법을 통해 입력값 받아오면 \n값도 같이 불러오기때문에 rstrip을 뒤에 붙여줌으로서 문자열만 받아올수 있다.
  '''