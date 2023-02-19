import argparse

from sqlalchemy.exc import IntegrityError

from session import Students, Teachers, Groups, Lessons, Grades
from session import session

pars = argparse.ArgumentParser()
pars.add_argument('--model', help='Select the table you want to add information to (Students, Teachers, Groups, Lessons, Grades')
pars.add_argument('--student_name')
pars.add_argument('--group_name')
pars.add_argument('--lesson_name')
pars.add_argument('--teacher_name')
pars.add_argument('--grade')
pars.add_argument('--student_id')
pars.add_argument('--group_id')
pars.add_argument('--lesson_id')
pars.add_argument('--teacher_id')


def teachers_insert():
    try:
        teacher = Teachers(teacher_name=arg_parser.teacher_name)
        session.add(teacher)
        session.commit()
    except IntegrityError:
        print('Not enough information.')


def students_insert():
    try:
        student = Students(student_name=arg_parser.student_name,
                           student_group_id=int(arg_parser.group_id))
        session.add(student)
        session.commit()
    except IntegrityError:
        print('Not enough information.')
    except ValueError:
        print(f'--group_id must be int')


def groups_insert():
    try:
        group = Groups(group_name=arg_parser.group_name)
        session.add(group)
        session.commit()
    except IntegrityError:
        print('Not enough information.')


def lessons_insert():
    try:
        lesson = Lessons(lesson_name=arg_parser.lesson_name,
                         teacher_id=int(arg_parser.teacher_id))
        session.add(lesson)
        session.commit()
    except IntegrityError:
        print('Not enough information.')
    except ValueError:
        print('--lesson_id must be int')


def grades_insert():
    try:
        grade = Grades(student_id=int(arg_parser.student_id),
                       lesson_id=int(arg_parser.lesson_id),
                       grade=int(arg_parser.grade))
        session.add(grade)
        session.commit()
    except IntegrityError:
        print('Not enough information.')
    except ValueError:
        print('--lesson_id, student_id and grade must be int')


TABLES = {'Teachers': teachers_insert,
          'Students': students_insert,
          'Groups': groups_insert,
          'Lessons': lessons_insert,
          'Grades': grades_insert}

if __name__ == '__main__':
    arg_parser = pars.parse_args()
    try:
        TABLES[arg_parser.model]()
    except KeyError:
        print(f'I cant find this model: {arg_parser.model}')
