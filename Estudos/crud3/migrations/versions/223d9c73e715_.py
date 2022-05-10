"""empty message

Revision ID: 223d9c73e715
Revises: 
Create Date: 2022-05-10 11:24:22.610939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '223d9c73e715'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('author', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
