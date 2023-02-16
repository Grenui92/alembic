from session import session
from create_data import Students, Groups, Lessons, Teachers, Grades
from sqlalchemy import func, desc
from sqlalchemy.dialects.postgresql import aggregate_order_by


def select_1():
    result = (
        session.query(Students.student_name, func.round(func.avg(Grades.grade), 2).label('AVG'))
        .select_from(Grades)
        .join(Students)
        .group_by(Students.student_id)
        .order_by(desc('AVG'))
        .limit(5)
        .all()
    )

    return result


def select_2():
    sub = (
        session.query(func.round(func.avg(Grades.grade), 2).label('AVG'),
                      Lessons.lesson_name.label('lesson'),
                      Students.student_name.label('students'))
        .select_from(Grades)
        .join(Lessons)
        .join(Students)
        .group_by(Lessons.lesson_name, Students.student_name)
        .subquery()
    )

    result = (
        session.query(sub.c.lesson,
                      func.max(sub.c.AVG),
                      func.array_agg(aggregate_order_by(sub.c.students, sub.c.AVG.desc()))[1])
        .select_from(sub)
        .group_by(sub.c.lesson)
        .all()
    )

    return result


def select_3():
    result = (
        session.query(func.round(func.avg(Grades.grade), 2),
                      Lessons.lesson_name)
        .select_from(Grades)
        .join(Lessons)
        .group_by(Lessons.lesson_name)
        .all()
    )

    return (result)


def select_4():
    result = (
        session.query(func.round(func.avg(Grades.grade).label('AVG grade'), 2))
        .select_from(Grades)
        .all()
    )

    return result


def select_5():
    result = (
        session.query(Teachers.teacher_name,
                      func.array_agg(Lessons.lesson_name))
        .select_from(Teachers)
        .join(Lessons)
        .group_by(Teachers.teacher_name)
        .all()
    )

    return result


def select_6():
    result = (
        session.query(Groups.group_name,
                      func.array_agg(Students.student_name))
        .select_from(Groups)
        .join(Students)
        .group_by(Groups.group_name)
        .all()
    )

    return result


def select_7():
    g_n = input('Enter group name: ')
    l_n = input('Enter lesson name: ')
    result = (
        session.query(Groups.group_name,
                      Students.student_name,
                      Lessons.lesson_name,
                      Grades.grade)
        .select_from(Grades)
        .join(Students)
        .join(Lessons)
        .join(Groups)
        .filter(Groups.group_name == g_n,
                Lessons.lesson_name == l_n)
        .order_by(Students.student_name)
        .all()
    )
    return result


def select_8():
    name = input('Enter teacher name: ')
    result = (session.query(Teachers.teacher_name,
                            Lessons.lesson_name,
                            func.round(func.avg(Grades.grade), 2))
              .select_from(Grades)
              .join(Lessons)
              .join(Teachers)
              .group_by(Teachers.teacher_name, Lessons.lesson_name)
              .filter(Teachers.teacher_name == name)
              .all())
    return result


def select_9():
    s_n = input('Enter student name: ')
    result = (session.query(Lessons.lesson_name)
              .select_from(Grades)
              .join(Lessons)
              .join(Students)
              .group_by(Lessons.lesson_name)
              .filter(Students.student_name == s_n)
              .all()
              )
    return result


def select_10():
    result = (session.query(Students.student_name,
                            Lessons.lesson_name,
                            Teachers.teacher_name)
              .select_from(Grades)
              .join(Students)
              .join(Lessons)
              .join(Teachers)
              .group_by(Students.student_name, Lessons.lesson_name, Teachers.teacher_name)
              .filter(Students.student_name == 'Daniel Powell',
                      Teachers.teacher_name == 'Madison Wagner')
              .all()
              )
    return result


if __name__ == '__main__':

    data = select_10()

    if isinstance(data, list):

        for rec in data:
            print(*rec)
    else:
        print(type(data))
