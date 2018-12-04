from mongo import db

student = db.student
course = db.course

print('找出年龄小于20岁且是软件学院的学生:')
task_2_result = student.find({'AGE': {'$lt': 20}, 'DNAME': '软件学院'})
# print(task_2_result)
for result in task_2_result:
    print(result)


print('\n检索先行课号为“300001”的课程名')
task_7_result = course.find({'FCID': 300001}, {'_id': 0, 'NAME': 1})
# print(task_7_result)
for result in task_7_result:
    print(result)
