n, k = map(int,input().split())
# input()으로 들어온 값을 split()으로 나눠서 int 로 변환 해준 뒤 맵으로 묶어준 것을 각각 n과 k에 넣는다.
cnt = 0
#갯수를 세야하니까 cnt 변수를 하나 지정해준다.
for i in range(1,n+1):
# 1부터 시작해서 n만큼의 길이만큼 반복문을 돌리는데
    if n%i == 0:
        #만약 n나누기 i 가 0과 같다면 cnt에 하나씩 더하며 넣어준다.
        cnt +=1
    if cnt == k:
        #만약 cnt 값이 k와 같다면 i를 프린트 하고 함수를 빠져나온다.
        print(i)
        break
else:
    #만약 걸리는 k 값이 없다면 -1을 프린트해준다.
    print(-1)