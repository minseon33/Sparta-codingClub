#문자열과 내장함수

msg = "It is Time"
# 문자열을 소문자화
print(msg.lower())
#문자열을 대문자화
print(msg.upper())
print(msg)

print("----------------------------------------")
tmp=msg.upper()
print(tmp)

# 문자열을 찾아서 인덱스값을 반환하는 find함수
print(tmp.find('T'))
#find는 처음 발견한 T의 인덱스번호를 출력해준다.

#문자열을 찾아 몇개인지 세어주는 count함수
print(tmp.count('T'))