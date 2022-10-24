from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.aik73au.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

# 데이터 하나 insert
# db.users.insert_one({'name':'bob', 'age':27})
# db.users.insert_one({'name':'john', 'age':20})
# db.users.insert_one({'name':'ann', 'age':20})

# ---------------- 데이터 하나 삭제
# db.users.delete_one({'name':'bob'})
# db.users.insert_one({'name':'bobby', 'age':27})

#-----------데이터 SELECT * FROM
# all_users = list(db.users.find({},{'_id':False}))
#
# for user in all_users:
#     print(user)
#------------------하나의 데이터 찾기
# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)
# print(user['age'])
# ------------------ 데이터 수정
# name이 bobby 인것을 찾아서, age를 19로 바꿔라~~~
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)
#------------------ 데이터 삭제
# db.users.delete_one({'name':'bobby'})
#
# all_users = list(db.users.find({},{'_id':False}))
#
# for user in all_users:
#     print(user)

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})


