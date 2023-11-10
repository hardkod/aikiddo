from typing import List

from sqlalchemy.orm import Session

from . import models, schemas


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students_by_parent_id(db: Session, parent_id: int):
    return db.query(models.Student).filter(models.Student.parent_id == parent_id).all()


def add_student(db: Session, student: schemas.StudentBaseSchema):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def remove_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False


def add_student_interests(db: Session, student_id: int, interests: List[schemas.InterestBaseSchema]):
    for interest_data in interests:
        db_interest = models.Interest(student_id=student_id, **interest_data.model_dump())
        db.add(db_interest)
    db.commit()


def add_student_pets(db: Session, student_id: int, pets: List[schemas.PetBaseSchema]):
    for pet_data in pets:
        db_pet = models.Pet(student_id=student_id, **pet_data.model_dump())
        db.add(db_pet)
    db.commit()


def add_student_lessons(db: Session, student_id: int, lessons: List[schemas.LessonBaseSchema]):
    for lesson_data in lessons:
        db_lesson = models.Lesson(student_id=student_id, **lesson_data.model_dump())
        db.add(db_lesson)
    db.commit()
