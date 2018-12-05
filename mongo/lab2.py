from mongo import db

course = db.student_course
print(course.count_documents({}))
# results = course.find()
# print(results.count())
# for r in results:
#     print(r)
