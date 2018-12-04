from mongo import db

student = db.student
course = db.course
teacher = db.teacher

print('向学生表中插入一条数据：')
student_data = {
    'SID': 201600301111,
    'NAME': '张三',
    'SEX': '男',
    'CLASS': 2016
}
task1_result = student.insert_one(student_data)
print(task1_result)

print('向课程表中插入一条数据：')
course_data = {
    'CID': 666666,
    'NAME': '中学物理'
}
task2_result = course.insert_one(course_data)
print(task2_result.inserted_id)

print('向教师表中插入多条数据：')
teacher_datas = [
    {
        'TID': 666666,
        'NAME': '张三',
        'DNAME': '软件学院'
    },
    {
        'TID': 777777,
        'AGE': 54,
        'NAME': '李四'
    }
]
task3_results = teacher.insert_many(teacher_datas)
print(task3_results)
print(task3_results.inserted_ids)
