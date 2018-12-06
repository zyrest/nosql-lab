from hbase import db

student = db['student']

student.delete('row-key')
