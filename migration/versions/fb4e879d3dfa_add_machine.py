"""Add machine

Revision ID: fb4e879d3dfa
Revises: 5982147a255e
Create Date: 2020-08-25 10:43:10.234188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb4e879d3dfa'
down_revision = '5982147a255e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('machine',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('machine')
    # ### end Alembic commands ###