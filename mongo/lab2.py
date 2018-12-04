from mongo import db

course = db.course

print(course.find_one())
