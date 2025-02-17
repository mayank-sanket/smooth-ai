from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class BuyerJourneyBaseSchema(BaseModel):
    title: str
    description: Optional[str] = None


class BuyerJourneyCreateSchema(BuyerJourneyBaseSchema):
    user_id: int


class BuyerJourneyReadSchema(BuyerJourneyBaseSchema):
    journey_id: int
    created_at: datetime



class BuyerJourneyQuestionsBaseSchema(BaseModel):
    question_text: str
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    is_permanent: Optional[bool] = True


class ListResponseQuestionSchema(BaseModel):
    code: str
    status: int
    response: List[BuyerJourneyQuestionsBaseSchema]

class BuyerJourneyQuestionsCreateSchema(BuyerJourneyQuestionsBaseSchema):
    journey_id: int


class BuyerJourneyQuestionsReadSchema(BuyerJourneyQuestionsBaseSchema):
    question_id: int
    created_at: datetime


class BuyerJourneyResponsesBaseSchema(BaseModel):
    response_text: str


class BuyerJourneyResponsesCreateSchema(BuyerJourneyResponsesBaseSchema):
    question_id: int
    user_id: int


class BuyerJourneyResponsesReadSchema(BuyerJourneyResponsesBaseSchema):
    response_id: int
    created_at: datetime


class BuyerJourneySubmissionBaseSchema(BaseModel):
    is_completed: bool


class BuyerJourneySubmissionCreateSchema(BuyerJourneySubmissionBaseSchema):
    journey_id: int
    user_id: int


class BuyerJourneySubmissionReadSchema(BuyerJourneySubmissionBaseSchema):
    submission_id: int
    created_at: datetime


class UpdateQuestionSchema(BaseModel):
    question_text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    is_permanent: Optional[bool] = None

    class Config:
        orm_mode = True