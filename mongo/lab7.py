from mongo import db

student = db.student
course = db.course
teacher = db.teacher
student_course = db.student_course
teacher_course = db.teacher_course

task4_condition = [
    {
        "$lookup": {
            "localField": "CID",
            "from": "course",
            "foreignField": "CID",
            "as": "course"
        }
    },
    {"$unwind": "$course"},
    {
        "$lookup": {
            "localField": "SID",
            "from": "student",
            "foreignField": "SID",
            "as": "student"
        }

    },
    {"$unwind": "$student"},
    {
        "$group": {
            "_id": "$SID",
            "name": {"$last": "$student.NAME"},
            "max_score": {"$max": "$SCORE"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "max_score": 1
        }
    }
]
task4_results = student_course.aggregate(task4_condition)
print(task4_results)
count = 0
for result in task4_results:
    print(result)
    count += 1
print('总计查询出{}条数据'.format(count))


task9_condition = [
    {
        "$lookup": {
            "from": "course",
            "localField": "CID",
            "foreignField": "CID",
            "as": "course"
        }
    },
    {"$unwind": "$course"},
    {
        "$group": {
            "_id": "$CID",
            "name": {"$last": "$course.NAME"},
            "select_count": {"$sum": 1}
        }
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "select_count": 1
        }
    },
    {"$sort": {"select_count": -1}},
    {"$limit": 10},
]
task9_results = student_course.aggregate(task9_condition)
count = 0
for result in task9_results:
    print(result)
    count += 1
print('总计查询出{}条数据'.format(count))
