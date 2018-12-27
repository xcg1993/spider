from pymongo import MongoClient
conn=MongoClient('10.12.155.22',27017)
print('成功')
db=conn.zhaopin
jobs=db.jobs

