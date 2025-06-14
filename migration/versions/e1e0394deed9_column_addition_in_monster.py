"""column addition in monster

Revision ID: e1e0394deed9
Revises: 81e424c2f09e
Create Date: 2025-06-15 14:55:22.226594

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1e0394deed9'
down_revision: Union[str, None] = '81e424c2f09e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monsters', sa.Column('type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('monsters', 'type')
    # ### end Alembic commands ###
