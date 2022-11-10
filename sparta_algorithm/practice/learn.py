num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
even_num = []
odd_num = []
sum_num = 0
for num in num_list:
    if num%2 == 0:
        print("짝수입니다.")
        even_num.append(num)
    else :
        print("홀수입니다.")
        odd_num.append(num)

print(len(even_num))
print(len(odd_num))

for num in num_list:
    sum_num += num

print(sum_num)

max_num = 0

for num in num_list:
    if num > max_num:
        max_num = num

print(max_num)
