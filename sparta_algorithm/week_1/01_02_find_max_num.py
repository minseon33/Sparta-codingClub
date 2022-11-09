# 각 숫자마다 모든 다른 숫자와 비교해서 최대값인지 확인합니다.
# 만약 다른 모든 값보다 크다면 반복문을 중단합니다.
# (비교를 위해 조금 이상하게 구현했습니다. 앞으로 이 강의를 들으면 이렇게 작성하지 않으실 거예요!)


input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

result = find_max_num(input)
print(result)