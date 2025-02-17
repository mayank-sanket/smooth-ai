"""Initial Migration

Revision ID: d4272a66cf99
Revises: 
Create Date: 2024-09-10 00:29:33.990509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd4272a66cf99'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('buyer_journey_responses')
    # op.drop_table('users')
    # op.drop_table('buyer_journey')
    # op.drop_table('buyer_journey_questions')
    # op.drop_table('buyer_journey_submission')
    # # ### end Alembic commands ###

def downgrade() -> None:
    op.create_table('buyer_journey_submission',
        sa.Column('submission_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('journey_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('is_completed', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['journey_id'], ['buyer_journey.journey_id'], name='buyer_journey_submission_journey_id_fkey'),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='buyer_journey_submission_user_id_fkey'),
        sa.PrimaryKeyConstraint('submission_id', name='buyer_journey_submission_pkey')
        )
    op.create_table('buyer_journey_questions',
        sa.Column('question_id', sa.INTEGER(), server_default=sa.text("nextval('buyer_journey_questions_question_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('journey_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('question_text', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('is_permanent', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['journey_id'], ['buyer_journey.journey_id'], name='buyer_journey_questions_journey_id_fkey'),
        sa.PrimaryKeyConstraint('question_id', name='buyer_journey_questions_pkey'),
        postgresql_ignore_search_path=False
        )
    op.create_table('buyer_journey',
        sa.Column('journey_id', sa.INTEGER(), server_default=sa.text("nextval('buyer_journey_journey_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='buyer_journey_user_id_fkey'),
        sa.PrimaryKeyConstraint('journey_id', name='buyer_journey_pkey'),
        postgresql_ignore_search_path=False
        )
    op.create_table('users',
        sa.Column('user_id', sa.INTEGER(), server_default=sa.text("nextval('users_user_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column('role', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
        sa.Column('package', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('user_id', name='users_pkey'),
        sa.UniqueConstraint('email', name='users_email_key'),
        postgresql_ignore_search_path=False
        )
    op.create_table('buyer_journey_responses',
        sa.Column('response_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('question_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('response_text', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['question_id'], ['buyer_journey_questions.question_id'], name='buyer_journey_responses_question_id_fkey'),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='buyer_journey_responses_user_id_fkey'),
        sa.PrimaryKeyConstraint('response_id', name='buyer_journey_responses_pkey')
        )
    # ### end Alembic commands ###
