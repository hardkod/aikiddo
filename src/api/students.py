from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from db.crud import add_student, remove_student, add_student_lessons, add_student_pets, \
    add_student_interests, get_student_by_id
from db.provider import get_db
from db.schemas import StudentSchema, StudentBaseSchema, PetBaseSchema, InterestBaseSchema, LessonBaseSchema

router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Student not found"}},
)


@router.post("/", response_model=StudentSchema,
             summary="Create a student",
             description="Create a student with basic information, without dependencies",
             operation_id="create_student"
             )
def create_student(student: StudentBaseSchema, db: Session = Depends(get_db)):
    return add_student(db=db, student=student)


@router.get("/{student_id}", response_model=StudentSchema,
            summary="Get student",
            description="Get student with all dependencies",
            operation_id="get_student"
            )
def read_student(student_id: str, db: Session = Depends(get_db)):
    db_student = get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# Endpoint to remove a student
@router.delete("/{student_id}",
               summary="Delete student",
               description="Deletes a student with all dependencies",
               operation_id="delete_student")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    if not remove_student(db, student_id=student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student removed"}


# Endpoint to add interests to a student
@router.post("/{student_id}/interests", response_model=StudentSchema, summary="Create student's interests",
             description="Create interests for a student identified by student_id",
             operation_id="create_student_interests")
def create_student_interests(student_id: str, interests: List[InterestBaseSchema], db: Session = Depends(get_db)):
    add_student_interests(db, student_id, interests)
    db_student = get_student_by_id(db, student_id=student_id)
    return db_student


# Endpoint to add pets to a student
@router.post("/{student_id}/pets", response_model=StudentSchema, summary="Create student's pets",
             description="Create pets for a student identified by student_id",
             operation_id="create_student_pets")
def create_student_pets(student_id: str, pets: List[PetBaseSchema], db: Session = Depends(get_db)):
    add_student_pets(db, student_id, pets)
    db_student = get_student_by_id(db, student_id=student_id)
    return db_student


# Endpoint to add lessons to a student
@router.post("/{student_id}/lessons", response_model=StudentSchema, summary="Create student's lessons",
             description="Create lessons for a student identified by student_id",
             operation_id="create_student_lessons")
def create_student_lessons(student_id: str, lessons: List[LessonBaseSchema], db: Session = Depends(get_db)):
    add_student_lessons(db, student_id, lessons)
    db_student = get_student_by_id(db, student_id=student_id)
    return db_student
