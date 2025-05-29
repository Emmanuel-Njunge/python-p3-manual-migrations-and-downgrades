"""Rename name to full_name in students

Revision ID: efe7aa4b0c02
Revises: 
Create Date: 2025-05-29 14:03:15.504788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efe7aa4b0c02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('students') as batch_op:
        batch_op.alter_column('name', new_column_name='full_name')


def downgrade() -> None:
    with op.batch_alter_table('students') as batch_op:
        batch_op.alter_column('full_name', new_column_name='name')
