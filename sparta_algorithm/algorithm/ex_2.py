# 로그인 문제 다시
id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
answer = ''
s_list=[]
for x in db:
    print(x)
    if x[0] == id_pw[0]:
        if x[1] == id_pw[1]:
            s_list.append("login")
            break
        elif x[1] != id_pw[1]:
            s_list.append("wrong pw")
            break
    elif x[0] != id_pw[0]:
        s_list.append("fail")
print(s_list)
answer = s_list[-1]
print(answer)
