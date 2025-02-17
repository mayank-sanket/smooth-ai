from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config import get_db
from schemas.buyer_journey import (
    BuyerJourneyCreateSchema, BuyerJourneyReadSchema, 
    BuyerJourneyQuestionsCreateSchema, BuyerJourneyQuestionsReadSchema,
    BuyerJourneyResponsesCreateSchema, BuyerJourneyResponsesReadSchema,
    BuyerJourneySubmissionCreateSchema, BuyerJourneySubmissionReadSchema,
    ListResponseQuestionSchema, UpdateQuestionSchema
)
import database.buyer_journey as journey_crud

buyer_journey_router = APIRouter(
    prefix="/buyer_journey",
    
)


# Create a new Buyer Journey
@buyer_journey_router.post("/", response_model=BuyerJourneyReadSchema, status_code=status.HTTP_201_CREATED)
def create_buyer_journey(buyer_journey: BuyerJourneyCreateSchema, db: Session = Depends(get_db)):
    return journey_crud.create_buyer_journey(db, buyer_journey)


# Create a new question for a Buyer Journey
@buyer_journey_router.post("/questions/", response_model=BuyerJourneyQuestionsReadSchema, status_code=status.HTTP_201_CREATED)
def create_buyer_journey_question(question: BuyerJourneyQuestionsCreateSchema, db: Session = Depends(get_db)):
    return journey_crud.create_buyer_journey_question(db, question)


@buyer_journey_router.get("/questions/permanent", response_model=ListResponseQuestionSchema)
def get_permanent_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = journey_crud.get_permanent_questions(db, skip=skip, limit=limit)
    return {"code": "success", "status": status.HTTP_200_OK, "response": questions}


@buyer_journey_router.get("/questions/user/{user_id}", response_model=ListResponseQuestionSchema)
def get_questions_by_user(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = journey_crud.get_questions_by_user_id(db, user_id=user_id, skip=skip, limit=limit)
    return {"code": "success", "status": status.HTTP_200_OK, "response": questions}

# Create a new response for a question
@buyer_journey_router.post("/responses/", response_model=BuyerJourneyResponsesReadSchema, status_code=status.HTTP_201_CREATED)
def create_buyer_journey_response(response: BuyerJourneyResponsesCreateSchema, db: Session = Depends(get_db)):
    return journey_crud.create_buyer_journey_response(db, response)


# Create a submission entry for a Buyer Journey
@buyer_journey_router.post("/submission/", response_model=BuyerJourneySubmissionReadSchema, status_code=status.HTTP_201_CREATED)
def create_buyer_journey_submission(submission: BuyerJourneySubmissionCreateSchema, db: Session = Depends(get_db)):
    return journey_crud.create_buyer_journey_submission(db, submission)

@buyer_journey_router.delete("/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    success = buyer_journey.delete_question(db, question_id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"code": "success", "status": status.HTTP_200_OK, "message": "Question deleted successfully"}

@buyer_journey_router.put("/questions/{question_id}", response_model=UpdateQuestionSchema)
def update_question(question_id: int, question_update: UpdateQuestionSchema, db: Session = Depends(get_db)):
    updated_question = buyer_journey.update_question(db, question_id, question_update.dict(exclude_unset=True))
    if not updated_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"code": "success", "status": status.HTTP_200_OK, "response": updated_question}