"""Added buyer journey tables with optionse

Revision ID: 94d5e3ff2c07
Revises: d4272a66cf99
Create Date: 2024-09-10 01:04:58.378667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '94d5e3ff2c07'
down_revision: Union[str, None] = 'd4272a66cf99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('buyer_journey_questions', sa.Column('option_a', sa.String(length=255), nullable=True))
    op.add_column('buyer_journey_questions', sa.Column('option_b', sa.String(length=255), nullable=True))
    op.add_column('buyer_journey_questions', sa.Column('option_c', sa.String(length=255), nullable=True))
    op.add_column('buyer_journey_questions', sa.Column('option_d', sa.String(length=255), nullable=True))

def downgrade():
    pass