from session import session
from session import Students, Grades, Teachers, Lessons, Groups
import faker
import random

def main():

    lessons_name = ['math', 'biology', 'literature', 'cinema', 'physic']
    groups = ['first', 'second', 'third', 'fourth', 'fifth']
    fak_data = faker.Faker()
    for gr in groups:
        gro = Groups(group_name=gr)
        session.add(gro)
        session.commit()
    for _ in range(5):
        teach = Teachers(teacher_name=fak_data.name())
        session.add(teach)
        session.commit()
    for les, num in zip(lessons_name, range(1, 6)):
        lesi = Lessons(lesson_name=les, teacher_id=num)
        session.add(lesi)
        session.commit()
    for _ in range(30):
        stud = Students(student_name=fak_data.name(), student_group_id=random.randrange(1, 6))
        session.add(stud)
        session.commit()
    for student in range(1, 31):
        for lesson in range(1, 6):
            for _ in range(5):
                grade = Grades(student_id=student, lesson_id=lesson, grade=random.randrange(1, 6))
                session.add(grade)
                session.commit()




if __name__ == '__main__':
    main()
