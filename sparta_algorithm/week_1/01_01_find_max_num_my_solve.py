input = [3, 5, 6, 1, 2, 4]


def find_max_num(input):
    max_num = 0
    print(input)
    for input_num in input:
        print("현재의 input_num 값 :" + str(input_num))
        if input_num > max_num:
            max_num = input_num
            print("현재의 max_num 값 : " + str(max_num))
    return max_num


result = find_max_num(input)
print(result)