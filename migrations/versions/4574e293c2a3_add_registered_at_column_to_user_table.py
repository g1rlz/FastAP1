"""Add registered_at column to user table

Revision ID: 4574e293c2a3
Revises: 03f7c8a7745c
Create Date: 2024-01-19 05:46:52.057621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4574e293c2a3'
down_revision: Union[str, None] = '03f7c8a7745c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_at', sa.TIMESTAMP(), nullable=True))
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.drop_column('user', 's_active')
    op.drop_column('user', 'timestamp')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('s_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'registered_at')
    # ### end Alembic commands ###
