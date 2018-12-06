from hbase import db

student = db['student']
course = db['course']
student_course = db['student_course']
sid = '0'


def data_input():
    global sid
    print('欢迎进入选课系统！')
    sid = str(input('请输入你的学号：'))
    # sid = '200900130985'


def course_output():
    selected_courses = student_course.scan(row_prefix=sid.encode('utf8'))
    print('\n以下为你目前选择的课程：')
    print('########################')
    print('\t课程号\t课程名')
    for key, s_c in selected_courses:
        s_c = dict(s_c)
        cid = s_c[b'info:CID'].decode('utf8')
        oneC = course.row(cid)
        name = oneC[b'info:NAME'].decode('utf8')
        print('\t{}\t{}'.format(cid, name))
    print('########################\n')


def course_select(cid):
    select_course = course.row(cid)
    if len(select_course) == 0:
        print('该课程不存在，请重新输入！')
        return

    sc_data = {
        'info:SID': sid,
        'info:CID': cid
    }
    student_course.put(sc_data['info:SID']+':'+sc_data['info:CID'], sc_data)
    print('选课成功')
    course_output()


if __name__ == '__main__':
    data_input()
    course_output()
    target_cid = str(input('请输入你要选择的课程号（输入0终止）：'))
    while target_cid != '0':
        course_select(target_cid)
        target_cid = str(input('请输入你要选择的课程号（输入0终止）：'))
