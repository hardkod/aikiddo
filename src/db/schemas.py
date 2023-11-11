from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, UUID4, Field


class LessonQuestionBaseSchema(BaseModel):
    """
        Base schema for a lesson question. Includes the text of the question, the expected answer,
        the answer given by the student, and the score awarded. This schema serves as a foundation
        for more detailed lesson question schemas.
        """
    question_text: str = Field(..., description="The text of the question presented in the lesson.",
                               example="What is the capital of France?")
    expected_answer: str = Field(..., description="The expected answer for the question.", example="Paris")
    given_answer: Optional[str] = Field(..., description="The answer given by the student.", example="Paris")
    score: int = Field(..., description="The score awarded for the student's answer.", example=10)


class LessonQuestionSchema(LessonQuestionBaseSchema):
    """
        Detailed schema for a lesson question, extending the base schema with a unique identifier (UUID).
        This schema is used to represent a specific question within a lesson, including its scoring details.
        """
    id: UUID4 = Field(..., description="Unique identifier for the lesson question.",
                      example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        from_attributes = True


class LessonBaseSchema(BaseModel):
    """
        Base schema for a lesson. Contains the core content and date/time information of a lesson.
        This schema acts as a base for more comprehensive lesson schemas.
        """
    content: str = Field(..., description="The content or topic of the lesson.",
                         example="Introduction to French Language")
    date: datetime = Field(..., description="The date and time when the lesson is conducted.",
                           example="2023-04-01T09:00:00")


class LessonSchema(LessonBaseSchema):
    """
        Comprehensive schema for a lesson. Extends the base lesson schema with a unique identifier (UUID)
        and a list of associated lesson questions. Represents the full structure of a lesson, including its
        educational content and assessment components.
        """
    id: UUID4 = Field(..., description="Unique identifier for the lesson.",
                      example="123e4567-e89b-12d3-a456-426614174001")
    questions: List[LessonQuestionSchema] = Field(..., description="List of questions associated with the lesson.")

    class Config:
        from_attributes = True


class InterestBaseSchema(BaseModel):
    """
        Base schema for representing a student's interest or hobby. Includes a description of the interest.
        This schema forms the foundation for more detailed interest representations.
        """
    interest: str = Field(..., description="A description of the student's interest or hobby.", example="Astronomy")


class InterestSchema(InterestBaseSchema):
    """
        Detailed schema for a student's interest, adding a unique identifier (UUID) to the base interest schema.
        Used to uniquely identify and represent a specific interest or hobby of a student.
        """
    id: UUID4 = Field(..., description="Unique identifier for the student's interest.",
                      example="123e4567-e89b-12d3-a456-426614174003")

    class Config:
        from_attributes = True


class PetBaseSchema(BaseModel):
    """
        Base schema for a pet. Includes essential details about the pet, such as its type, breed (optional),
        and name. This schema serves as a base for more detailed pet representations.
        """
    pet_type: str = Field(..., description="The type of pet, such as 'Dog' or 'Cat'.", example="Dog")
    pet_breed: str = Field('', description="The breed of the pet, if applicable.",
                                     example="Golden Retriever")
    pet_name: str = Field(..., description="The name of the pet.", example="Buddy")


class PetSchema(PetBaseSchema):
    """
        Detailed schema for a pet, extending the base schema with a unique identifier (UUID).
        This schema is used to represent specific pets, providing unique identification and detailed information.
        """
    id: UUID4 = Field(..., description="Unique identifier for the pet.", example="123e4567-e89b-12d3-a456-426614174004")

    class Config:
        from_attributes = True


class StudentBaseSchema(BaseModel):
    """
        Base schema for a student. Contains core personal information about a student such as name,
        gender, birthdate, hair color, and hair type. Serves as a foundation for more detailed student schemas.
        """
    name: str = Field(..., description="The student's name.", example="John Doe")
    gender: str = Field(..., description="The student's gender.", examples=["Male", "Female"])
    birthdate: date = Field(..., description="The student's birthdate.", example="2014-08-02")
    hair_color: str = Field(..., description="The student's hair color.", example="Brown")
    hair_type: str = Field(...,
                           description="The student's hair type, such as 'Straight' or 'Curly', 'Long' or 'Short''",
                           example="Straight, Short")


class StudentSchema(StudentBaseSchema):
    """
        Comprehensive schema for a student. Extends the base schema with a unique identifier (UUID),
        and includes lists of interests, pets, and lessons associated with the student. Represents
        the full profile of a student in the educational context.
        """
    id: UUID4 = Field(..., description="Unique identifier for the student.",
                      example="123e4567-e89b-12d3-a456-426614174005")
    interests: List[InterestSchema] = Field([], description="List of the student's interests.")
    pets: List[PetSchema] = Field([], description="List of the student's pets.")
    lessons: List[LessonSchema] = Field([], description="List of lessons associated with the student.")

    class Config:
        from_attributes = True


class TestQuestionBaseSchema(BaseModel):
    """
        Base schema for a test question. Includes the test identifier, the text of the question, the expected
        answer, the given answer, and the score. This schema forms the foundation for detailed representations
        of test questions.
        """
    test_id: UUID4 = Field(..., description="Identifier for the test associated with this question.",
                           example="uuid-test-1")
    question_text: str = Field(..., description="The text of the test question.",
                               example="What is the capital of France?")
    expected_answer: str = Field(..., description="The expected answer for the test question.", example="Paris")
    given_answer: str = Field(..., description="The answer given by the student for the test question.",
                              example="Berlin")
    score: int = Field(..., description="The score awarded for the student's answer on this test question.", example=0)


class TestQuestionSchema(TestQuestionBaseSchema):
    """
        Detailed schema for a test question, adding a unique identifier (UUID) to the base test question schema.
        Used to represent specific questions within a test, complete with scoring and identification details.
        """
    id: UUID4 = Field(..., description="Unique identifier for the test question.",
                      example="123e4567-e89b-12d3-a456-426614174009")

    class Config:
        from_attributes = True


class LevelingTestBaseSchema(BaseModel):
    """
        Base schema for a leveling test. Includes the student identifier and the date/time of the test.
        Acts as a foundation for more comprehensive leveling test schemas.
        """
    student_id: UUID4 = Field(..., description="Identifier for the student taking the leveling test.",
                              example="uuid-student-1")
    date: datetime = Field(..., description="The date and time when the leveling test is conducted.",
                           example="2023-04-01T10:00:00")


class LevelingTestSchema(LevelingTestBaseSchema):
    """
        Comprehensive schema for a leveling test. Extends the base schema with a unique identifier (UUID)
        and a list of test questions. Represents the full structure of a leveling test, including its
        scheduling and assessment components.
        """
    id: UUID4 = Field(..., description="Unique identifier for the leveling test.",
                      example="123e4567-e89b-12d3-a456-426614174010")
    test_questions: List[TestQuestionSchema] = Field(...,
                                                     description="List of questions associated with the leveling test.")

    class Config:
        from_attributes = True
