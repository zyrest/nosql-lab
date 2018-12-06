from hbase import db

student = db['student']

lalala = 'a:b:c'
print(lalala.split(':')[2])
