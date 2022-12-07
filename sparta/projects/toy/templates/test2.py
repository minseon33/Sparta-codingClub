def solution(a, b):
    answer = 0
    최대공약수 = 0
    # 공약수 구하기
    n = b
    for x in range(1, a+1):
        if a%x == 0 and b%x == 0:
            최대공약수 = x
    print(최대공약수)
    a = a//최대공약수
    b = b//최대공약수
    print(f'a:{a}  b:{b}')
    # 유한소수 구하기
    while b % 2 == 0 or b % 5 == 0:
        b = b//2
        print(f'2로 나눈 b: {b}')

    if b == 1:
        answer = 1
    else:
        answer = 2

    print(f'answer 의 값 : {answer}')
    return answer

# 기약분수 만들기 > a,b의 최대공약수로 약분
# 소인수분해 하기 >소인수가 2와 5만 존재하면 유한소수
# if 문 쓰기  > 유한소수면 1, 무한소수면 2 리턴


solution(12,21)

