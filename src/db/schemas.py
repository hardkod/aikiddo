from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, UUID4, Field


class LessonQuestionBaseSchema(BaseModel):
    question_text: str = Field(..., description="The text of the question presented in the lesson.")
    expected_answer: str = Field(..., description="The expected answer for the question.")
    given_answer: str = Field(..., description="The answer given by the student.")
    score: int = Field(..., description="The score awarded for the student's answer.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "question_text": "What is the capital of France?",
                "expected_answer": "Paris",
                "given_answer": "Paris",
                "score": 10
            }
        }
    }


class LessonQuestionSchema(LessonQuestionBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the lesson question.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "question_text": "What is the capital of France?",
                    "expected_answer": "Paris",
                    "given_answer": "Paris",
                    "score": 10
                }
            ]
        }



class LessonBaseSchema(BaseModel):
    content: str = Field(..., description="The content or topic of the lesson.")
    date: datetime = Field(..., description="The date and time when the lesson is conducted.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "content": "Introduction to French Language",
                "date": "2023-04-01T09:00:00"
            }
        }
    }


class LessonSchema(LessonBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the lesson.")
    questions: List[LessonQuestionSchema] = Field(..., description="List of questions associated with the lesson.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174001",
                    "content": "French Revolution Overview",
                    "date": "2023-04-01T10:00:00",
                    "questions": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174002",
                            "question_text": "When did the French Revolution start?",
                            "expected_answer": "1789",
                            "given_answer": "1789",
                            "score": 10
                        }
                    ]
                }
            ]
        }



class InterestBaseSchema(BaseModel):
    interest: str = Field(..., description="A description of the student's interest or hobby.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "interest": "Astronomy"
            }
        }
    }


class InterestSchema(InterestBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the student's interest.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174003",
                    "interest": "Astronomy"
                }
            ]
        }



class PetBaseSchema(BaseModel):
    pet_type: str = Field(..., description="The type of pet, such as 'Dog' or 'Cat'.")
    pet_breed: Optional[str] = Field(None, description="The breed of the pet, if applicable.")
    pet_name: str = Field(..., description="The name of the pet.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "pet_type": "Dog",
                "pet_breed": "Golden Retriever",
                "pet_name": "Buddy"
            }
        }
    }


class PetSchema(PetBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the pet.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174004",
                    "pet_type": "Dog",
                    "pet_breed": "Golden Retriever",
                    "pet_name": "Buddy"
                }
            ]
        }



class StudentBaseSchema(BaseModel):
    name: str = Field(..., description="The student's name.")
    gender: str = Field(..., description="The student's gender.")
    birthdate: date = Field(..., description="The student's birthdate.")
    hair_color: str = Field(..., description="The student's hair color.")
    hair_type: str = Field(...,
                           description="The student's hair type, such as 'Straight' or 'Curly', 'Long' or 'Short''")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Doe",
                "gender": "Male",
                "birthdate": "2010-01-01",
                "hair_color": "Brown",
                "hair_type": "Straight, Short"
            }
        }
    }


class StudentSchema(StudentBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the student.")
    interests: Optional[List[InterestSchema]] = Field(None, description="List of the student's interests.")
    pets: Optional[List[PetSchema]] = Field(None, description="List of the student's pets.")
    lessons: Optional[List[LessonSchema]] = Field(None, description="List of lessons associated with the student.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174005",
                    "name": "John Doe",
                    "gender": "Male",
                    "birthdate": "2010-01-01",
                    "hair_color": "Brown",
                    "hair_type": "Straight",
                    "interests": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174006",
                            "interest": "Robotics"
                        }
                    ],
                    "pets": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174007",
                            "pet_type": "Cat",
                            "pet_breed": "Siamese",
                            "pet_name": "Whiskers"
                        }
                    ],
                    "lessons": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174008",
                            "content": "Basic Algebra",
                            "date": "2023-04-05T09:00:00",
                            "questions": []
                        }
                    ]
                }
            ]
        }


class TestQuestionBaseSchema(BaseModel):
    test_id: UUID4 = Field(..., description="Identifier for the test associated with this question.")
    question_text: str = Field(..., description="The text of the test question.")
    expected_answer: str = Field(..., description="The expected answer for the test question.")
    given_answer: str = Field(..., description="The answer given by the student for the test question.")
    score: int = Field(..., description="The score awarded for the student's answer on this test question.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "test_id": "uuid-test-1",
                "question_text": "What is the largest planet in our Solar System?",
                "expected_answer": "Jupiter",
                "given_answer": "Saturn",
                "score": 5
            }
        }
    }


class TestQuestionSchema(TestQuestionBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the test question.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174009",
                    "test_id": "uuid-test-1",
                    "question_text": "What is the boiling point of water?",
                    "expected_answer": "100°C",
                    "given_answer": "100°C",
                    "score": 10
                }
            ]
        }


class LevelingTestBaseSchema(BaseModel):
    student_id: UUID4 = Field(..., description="Identifier for the student taking the leveling test.")
    date: datetime = Field(..., description="The date and time when the leveling test is conducted.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "student_id": "uuid-student-1",
                "date": "2023-04-01T10:00:00"
            }
        }
    }


class LevelingTestSchema(LevelingTestBaseSchema):
    id: UUID4 = Field(..., description="Unique identifier for the leveling test.")
    test_questions: List[TestQuestionSchema] = Field(...,
                                                     description="List of questions associated with the leveling test.")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174010",
                    "student_id": "123e4567-e89b-12d3-a456-426614174011",
                    "date": "2023-04-01T10:00:00",
                    "test_questions": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174012",
                            "test_id": "uuid-test-1",
                            "question_text": "What is the capital of Spain?",
                            "expected_answer": "Madrid",
                            "given_answer": "Madrid",
                            "score": 10
                        },
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174013",
                            "test_id": "uuid-test-1",
                            "question_text": "What is H2O commonly known as?",
                            "expected_answer": "Water",
                            "given_answer": "Water",
                            "score": 10
                        }
                    ]
                }
            ]
        }
