# 대표값 구하기

#입력예제 :
# 10
# 45 73 66 87 92 67 75 79 75 80

#출력예제 :
# 74  7


n = int(input())
a = list(map(int,input().split()))
ave = round(sum(a)/n)
min = 2147000000

for idx,x in enumerate(a):
    #a의 인덱스 값을 idx에 넣어주고 x에 a 리스트의 값을 넣어서 대응해주는 함수 enumerate()
    tmp = abs(x-ave)
    if tmp < min :
        min = tmp
        score = x
        res = idx+1 #학생번호 인데 인덱스가 0번부터 시작하니까 +1을 해주어야 한다.
    #답이 2개인 경우 구현
    elif tmp == min:
        if x>score :
            score = x
            res = idx + 1
print(ave, res)