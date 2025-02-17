from sqlalchemy.orm import Session
from models.buyer_journey import BuyerJourney, BuyerJourneyQuestions, BuyerJourneyResponses, BuyerJourneySubmission
from schemas.buyer_journey import BuyerJourneyCreateSchema, BuyerJourneyQuestionsCreateSchema, BuyerJourneyResponsesCreateSchema, BuyerJourneySubmissionCreateSchema


# Buyer Journey CRUD
def create_buyer_journey(db: Session, buyer_journey: BuyerJourneyCreateSchema):
    db_buyer_journey = BuyerJourney(**buyer_journey.dict())
    db.add(db_buyer_journey)
    db.commit()
    db.refresh(db_buyer_journey)
    return db_buyer_journey

def get_buyer_journey_by_id(db: Session, journey_id: int):
    return db.query(BuyerJourney).filter(BuyerJourney.journey_id == journey_id).first()


# Buyer Journey Questions CRUD
def create_buyer_journey_question(db: Session, question: BuyerJourneyQuestionsCreateSchema):
    db_question = BuyerJourneyQuestions(
        journey_id=question.journey_id,
        question_text=question.question_text,
        option_a=question.option_a,
        option_b=question.option_b,
        option_c=question.option_c,
        option_d=question.option_d,
        is_permanent=question.is_permanent,
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

# Buyer Journey Responses CRUD
def create_buyer_journey_response(db: Session, response: BuyerJourneyResponsesCreateSchema):
    db_response = BuyerJourneyResponses(**response.dict())
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    return db_response


# Buyer Journey Submission CRUD
def create_buyer_journey_submission(db: Session, submission: BuyerJourneySubmissionCreateSchema):
    db_submission = BuyerJourneySubmission(**submission.dict())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

def get_permanent_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BuyerJourneyQuestions).filter(BuyerJourneyQuestions.is_permanent == True).offset(skip).limit(limit).all()


def get_questions_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (db.query(BuyerJourneyQuestions)
            .join(BuyerJourney, BuyerJourneyQuestions.journey_id == BuyerJourney.journey_id)
            .filter(BuyerJourney.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all())

def delete_question(db: Session, question_id: int):
    question = db.query(BuyerJourneyQuestions).filter(BuyerJourneyQuestions.question_id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
        return True
    return False


def update_question(db: Session, question_id: int, question_data: dict):
    question = db.query(BuyerJourneyQuestions).filter(BuyerJourneyQuestions.question_id == question_id).first()
    if question:
        for key, value in question_data.items():
            setattr(question, key, value)
        db.commit()
        db.refresh(question)  # Refresh the instance to get the updated values
        return question
    return None