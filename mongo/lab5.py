from mongo import db

student = db.student
course = db.course
teacher = db.teacher

student_condition = {'SID': 201600301111}
student_data = student.find_one(student_condition)
student_data['CLASS'] = 2017
student_result = student.update_one(student_condition, {'$set': student_data})
print(student_result)

course_condition = {'CID': 666666}
course_result = course.update_one(course_condition, {'$set': {'NAME': '中学生物'}})
print(course_result)

teacher_condition = {'$where': 'obj.TID == 666666 || obj.TID == 777777'}
teacher_result = teacher.update_many(teacher_condition, {'$inc': {'AGE': 2}})
print(teacher_result)
