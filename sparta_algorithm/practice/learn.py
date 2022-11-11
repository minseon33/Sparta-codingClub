#문자열과 내장함수

msg = "It is Time"
# 문자열을 소문자화
print(msg.lower())
#문자열을 대문자화
print(msg.upper())
print(msg)

print("----------------------------------------")
tmp= msg.upper()
print(tmp)

# 문자열을 찾아서 인덱스값을 반환하는 find함수
print(tmp.find('T'))
#find는 처음 발견한 T의 인덱스번호를 출력해준다.

#문자열을 찾아 몇개인지 세어주는 count함수
print(tmp.count('T'))

#문자열을 잘라주는 슬라이스
print(msg)
#msg 문자열의 처음부터 2번째 글자까지만 뽑아내겠다~~
print(msg[:2])
# >> 인덱스 2번 바로 앞에서 자르겠다.. 즉, 0,1 까지만 출력되므로 2개 글자만 출력된다.
print(msg[3:5])
# >> 인덱스번호 3번부터 인덱스번호 5번 전까지 뽑아내겠다.. 즉, 인덱스번호 3번,4번까지만 출력됨.
print("----------------------------------------")
#문자열의 길이를 구해주는 len() 함수
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end='/')
print()
for x in msg:
    print(x, end='! ')
print()
# 문자열에서 대문자만 출력하기
for s in msg:
    if s.isupper():
        print(s, end="/")
print()
#문자열에서 소문자만 출력하기
for s in msg:
    if s.islower():
        print(s, end="/")
print()
#공백 제거하고 붙여서 출력하기
for x in msg:
    if x.isalpha():
        print(x,end="")
print()
print("----------------------------------------")
#아스키넘버 출력하는 ord()

tmp = 'AZ'
for x in tmp:
    print(ord(x))
print("****************************************")
tmp = 'az'
for z in tmp:
    print(ord(z))
print("****************************************")
#아스키넘버에 대응되는 문자를 출력해주는 chr()
tmp = 65
print(chr(tmp))
