"""
Create database

Revision ID: 33235f55faab
Revises: 
Create Date: 2022-05-5 11:39:29.055650
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '33235f55faab'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'news',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('header', sa.String, nullable=False),
        sa.Column('image', sa.String, nullable=False),
        sa.Column('item', sa.String, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('news')
