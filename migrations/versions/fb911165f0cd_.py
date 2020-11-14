"""empty message

Revision ID: fb911165f0cd
Revises: 
Create Date: 2020-11-14 00:54:03.581606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb911165f0cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('var1', sa.Integer(), nullable=True),
    sa.Column('var2', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Label')
    # ### end Alembic commands ###