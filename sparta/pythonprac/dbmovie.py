from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.aik73au.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta




movie = db.movies.find_one({'title':'가버나움'})

star = movie['star']
all_movie = list(db.movies.find({'star': star},{'_id':False}))
#>> find 괄호 안에 있는것들은 조건들..
# print(movie_ga['title'],movie_ga['star'])
# print(movie)

for m in all_movie:
    print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':"0"}})

for m in all_movie:
    print(m)



