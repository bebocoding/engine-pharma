"""add user details to users table

Revision ID: 0f2b65becc24
Revises: 961f62706897
Create Date: 2024-03-07 22:34:36.618572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f2b65becc24'
down_revision: Union[str, None] = '961f62706897'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('first_name', sa.String()))
    op.add_column('users',sa.Column('last_name', sa.String()))
    op.add_column('users',sa.Column('email', sa.String(),unique=True))
    op.add_column('users',sa.Column('address1', sa.String()))
    op.add_column('users',sa.Column('address2', sa.String()))
    op.add_column('users',sa.Column('country', sa.String()))
    op.add_column('users',sa.Column('city', sa.String()))
    op.add_column('users',sa.Column('district', sa.String()))
    pass


def downgrade() -> None:
    op.drop_column('users','first_name')
    op.drop_column('users','last_name')
    op.drop_column('users','email')
    op.drop_column('users','address1')
    op.drop_column('users','address2')
    op.drop_column('users','country')
    op.drop_column('users','city')
    op.drop_column('users','district')
    pass
