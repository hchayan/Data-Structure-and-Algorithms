# bubble sort

def bubbleSort(x):
  for i in range(len(x)-1):     
    for j in range(len(x)-1-i): # j의 탐색범위를 0~n, 0~n-1.. 로 줄여나간다.
      if x[j] > x[j+1]:         # 인접한 두수에서 작은수가 큰수보다 뒤에 있을때
        x[j],x[j+1] = x[j+1],x[j]
  return x

x= [5,2,8,6,1]
print(bubbleSort(x))