from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from database.mixins import TimestampMixin
from datetime import datetime


class BuyerJourney(Base, TimestampMixin):
    __tablename__ = "buyer_journey"

    journey_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    questions = relationship("BuyerJourneyQuestions", back_populates="journey")


class BuyerJourneyQuestions(Base, TimestampMixin):
    __tablename__ = "buyer_journey_questions"

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    journey_id = Column(Integer, ForeignKey("buyer_journey.journey_id"), nullable=False)
    question_text = Column(Text, nullable=False)
    option_a = Column(String(255), nullable=True)
    option_b = Column(String(255), nullable=True)
    option_c = Column(String(255), nullable=True)
    option_d = Column(String(255), nullable=True)
    is_permanent = Column(Boolean, default=True)  # Set to True as per your requirements
    created_at = Column(DateTime, default=datetime.utcnow)
    journey = relationship("BuyerJourney", back_populates="questions")
    responses = relationship("BuyerJourneyResponses", back_populates="question")



class BuyerJourneyResponses(Base, TimestampMixin):
    __tablename__ = "buyer_journey_responses"

    response_id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("buyer_journey_questions.question_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    response_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    question = relationship("BuyerJourneyQuestions", back_populates="responses")


class BuyerJourneySubmission(Base, TimestampMixin):
    __tablename__ = "buyer_journey_submission"

    submission_id = Column(Integer, primary_key=True, autoincrement=True)
    journey_id = Column(Integer, ForeignKey("buyer_journey.journey_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

