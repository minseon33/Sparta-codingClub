# 입력 예제 : 4 6

n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max = -2147000000
for i in range(1,n+1): #n+1 까지 해야 n까지 돌게된다. 왜냐하면 range() 함수는 0부터 n-1까지 도니까.. range(4)하면 0,1,2,3 이렇게 돔.
    for j in range(1,m+1): #주사위 눈이 1부터 시작하니까 1부터 돌아야 한다.
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end= ' ')