"""empty message

Revision ID: 060b740e71cb
Revises: 78b1fe77afc9
Create Date: 2023-08-10 18:44:43.508191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '060b740e71cb'
down_revision = '78b1fe77afc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###