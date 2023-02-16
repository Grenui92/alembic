from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from datetime import datetime

engine = create_engine('postgresql+psycopg2://postgres:92062555Vv@localhost:5432/postgres')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(250), nullable=False)
    student_group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='CASCADE'))
    group = relationship('Groups', backref='student')



class Groups(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(10), nullable=False)

class Teachers(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(30), nullable=False)

class Lessons(Base):
    __tablename__ = 'lessons'
    lesson_id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_name = Column(String(30), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id', ondelete='CASCADE'))
    teacher = relationship('Teachers', backref="lesson")

class Grades(Base):
    __tablename__ = 'grades'
    mark_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id', ondelete='CASCADE'))
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id', ondelete='CASCADE'))
    grade = Column(Integer, nullable=False)
    create_at = Column(TIMESTAMP, default=datetime.now())
    student = relationship('Students', backref='grade')
    lesson = relationship('Lessons', backref='grade')



if __name__ == '__main__':
    Base.metadata.create_all(engine)