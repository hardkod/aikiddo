import uuid

from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String, index=True)
    gender = Column(String)
    birthdate = Column(Date)
    hair_color = Column(String)
    hair_type = Column(String)
    interests = relationship("Interest", back_populates="student")
    pets = relationship("Pet", back_populates="student")
    lessons = relationship("Lesson", back_populates="student")


class Interest(Base):
    __tablename__ = "interests"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    student_id = Column(String, ForeignKey('students.id'))
    interest = Column(String)

    student = relationship("Student", back_populates="interests")

class Pet(Base):
    __tablename__ = "pets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    student_id = Column(String, ForeignKey('students.id'))
    pet_type = Column(String)
    pet_breed = Column(String)
    pet_name = Column(String)

    student = relationship("Student", back_populates="pets")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    student_id = Column(String, ForeignKey('students.id'))
    content = Column(Text)
    date = Column(DateTime)

    student = relationship("Student", back_populates="lessons")
    questions = relationship("LessonQuestion", back_populates="lesson")


class LessonQuestion(Base):
    __tablename__ = "lesson_questions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    lesson_id = Column(String, ForeignKey('lessons.id'))
    question_text = Column(Text)
    expected_answer = Column(Text)
    given_answer = Column(Text)
    score = Column(Integer)

    lesson = relationship("Lesson", back_populates="questions")


class LevelingTest(Base):
    __tablename__ = "leveling_tests"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    student_id = Column(String, ForeignKey('students.id'))
    date = Column(DateTime)

    student = relationship("Student")
    test_questions = relationship("TestQuestion", back_populates="test")


class TestQuestion(Base):
    __tablename__ = "test_questions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    test_id = Column(String, ForeignKey('leveling_tests.id'))
    question_text = Column(Text)
    expected_answer = Column(Text)
    given_answer = Column(Text)
    score = Column(Integer)

    test = relationship("LevelingTest", back_populates="test_questions")
