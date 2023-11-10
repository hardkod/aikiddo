from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, UUID4


class LessonQuestionBaseSchema(BaseModel):
    question_text: str
    expected_answer: str
    given_answer: str
    score: int


class LessonQuestionSchema(BaseModel):
    id: UUID4
    question_text: str
    expected_answer: str
    given_answer: str
    score: int


class LessonBaseSchema(BaseModel):
    content: str
    date: datetime


class LessonSchema(LessonBaseSchema):
    id: UUID4
    questions: List[LessonQuestionSchema] = []

    class Config:
        from_attributes = True


class InterestBaseSchema(BaseModel):
    interest: str


class InterestSchema(InterestBaseSchema):
    id: UUID4

    class Config:
        from_attributes = True


class PetBaseSchema(BaseModel):
    pet_type: str
    pet_breed: Optional[str] = None
    pet_name: str


class PetSchema(PetBaseSchema):
    id: UUID4

    class Config:
        from_attributes = True


class StudentBaseSchema(BaseModel):
    name: str
    gender: str
    birthdate: date
    hair_color: str
    hair_type: str


class StudentSchema(StudentBaseSchema):
    id: UUID4
    interests: Optional[List[InterestSchema]] = []
    pets: Optional[List[PetSchema]] = []
    lessons: Optional[List[LessonSchema]] = []

    class Config:
        from_attributes = True


class TestQuestionBaseSchema(BaseModel):
    test_id: str
    question_text: str
    expected_answer: str
    given_answer: str
    score: int


class TestQuestionSchema(TestQuestionBaseSchema):
    id: UUID4

    class Config:
        from_attributes = True


class LevelingTestBaseSchema(BaseModel):
    student_id: str
    date: datetime


class LevelingTestSchema(LevelingTestBaseSchema):
    id: UUID4
    test_questions: List[TestQuestionSchema] = []

    class Config:
        from_attributes = True

