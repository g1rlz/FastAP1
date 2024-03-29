"""initial

Revision ID: bc244bcc72c6
Revises: c0322967a35f
Create Date: 2024-01-19 08:20:12.280679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc244bcc72c6'
down_revision: Union[str, None] = 'c0322967a35f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('operation', 'instrument_type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('operation', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('operation', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('operation', 'instrument_type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
