# 배열 뒤집기
# num_list = [1,2,3,4,5]
# a = []
# for s in range(len(num_list)):
#     b = (len(num_list)-s)-1
#     a.append(num_list[b])
#     print(a)
# ------------------------------------------------------
# 문자열 뒤집기
# my_string = "jaron"
# b_list = []
#
# for a in range(len(my_string)):
#     x = (len(my_string)-1) - a
#     b_list.append(my_string[x])
#     print(''.join(b_list))
#---------------------------------------------------------

#삼각형의 완성조건(2)

# sides = [11,7]
# min_num = 0
# max_num = 0
# n , k = map(int,sides)
#
# if n < k :
#     min_num = n
#     max_num = k
# else:
#     max_num = n
#     min_num = k
#
# y = (max_num+min_num)-(max_num-min_num)-1
#
#
# print(n)
# print(k)
#
# print(min_num)
# print(max_num)
# print(y)
#---------------------------------------------------------
# 369 게임
# n = 3
# k = str(n)
# z = []
# count = 0
# for x in k:
#     z.append(x)
# print(z)
# for a in z:
#     if int(a) == 3 or int(a) == 6 or int(a) == 9:
#         count += 1
#
# print(count)
#---------------------------------------------------------
#로그인 성공?

# id_pw = ["meosseugi", "1234"]
# db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

# 1차시도
# for x in db :
#     for a in x:
#         if a == id_pw[0]
#             print("login")

#2차 시도
# lo = "login"
# pw = "wrong pw"
# fail = "fail"
# for x in db:
#     if x == id_pw:
#         print("login")
#     elif x[0] == id_pw[0] and x != id_pw[1]:
#         print("wrong pw")
#     elif x[0] != id_pw[0] and x[1] != id_pw[1]:
#         print("fail")

#3차 시도
id_pw = ["programmer01", "15789"]
db = 	[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

id = False
pw = False
s_list=[]
answer = ''

for x in db:
    for a in id_pw:
        if a == x[0]:
            id = True
        elif a == x[1]:
            pw = True

        if id == True and pw == True:
            s_list.append("login")
            break
        elif id == True and pw == False:
            s_list.append("wrong pw")
            break
        elif id == False:
            s_list.append("fail")
print(s_list)
answer = s_list[-1]
print(answer)

# 왜 안되는거야..!!!!!!! ㅠㅠㅠㅠ


#--------------------------------------------------
#369 다시






