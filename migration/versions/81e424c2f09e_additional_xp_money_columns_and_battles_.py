"""additional xp/money columns and battles table

Revision ID: 81e424c2f09e
Revises: 6e566ff404eb
Create Date: 2025-06-15 13:54:03.274657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81e424c2f09e'
down_revision: Union[str, None] = '6e566ff404eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('battle_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attacker_id', sa.Integer(), nullable=True),
    sa.Column('defender_id', sa.Integer(), nullable=True),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['attacker_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['defender_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('players', sa.Column('experience', sa.Integer(), nullable=True))
    op.add_column('players', sa.Column('money', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('players', 'money')
    op.drop_column('players', 'experience')
    op.drop_table('battle_history')
    # ### end Alembic commands ###
