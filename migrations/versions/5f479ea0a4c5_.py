"""empty message

Revision ID: 5f479ea0a4c5
Revises: 
Create Date: 2024-03-17 15:19:52.166389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f479ea0a4c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('propID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('descr', sa.String(length=120), nullable=True),
    sa.Column('numRooms', sa.Integer(), nullable=True),
    sa.Column('numBaths', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('propType', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('propID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
