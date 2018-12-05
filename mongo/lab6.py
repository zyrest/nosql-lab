from mongo import db

student_course = db.student_course
course = db.course
sid = 0


def data_input():
    global sid
    print('欢迎进入选课系统！')
    sid = int(input('请输入你的学号：'))
    # sid = 200900130985


def course_output():
    cids = student_course.find({'SID': sid}, {'_id': 0, 'CID': 1})
    print('\n以下为你目前选择的课程：')
    print('########################')
    print('\t课程号\t课程名')
    for cid in cids:
        cid = cid['CID']
        oneC = course.find_one({'CID': cid})
        print('\t{}\t{}'.format(oneC['CID'], oneC['NAME']))
    print('########################\n')


def course_select(cid):
    select_course = course.find_one({'CID': cid})
    if select_course is None:
        print('该课程不存在，请重新输入！')
        return

    sc_data = {
        'SID': sid,
        'CID': cid
    }
    result = student_course.insert_one(sc_data)
    print('选课成功')
    course_output()


if __name__ == '__main__':
    data_input()
    course_output()
    target_cid = int(input('请输入你要选择的课程号（输入0终止）：'))
    while target_cid != 0:
        course_select(target_cid)
        target_cid = int(input('请输入你要选择的课程号（输入0终止）：'))
