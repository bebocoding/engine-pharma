"""create users table

Revision ID: c885a5918f98
Revises: 
Create Date: 2024-03-07 21:16:07.767316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c885a5918f98'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('phone_number', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
