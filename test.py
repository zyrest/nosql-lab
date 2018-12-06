from hbase import db

student = db['student']

one = student.row(b'2189378921739812739')
print(one.__len__() == 0)
