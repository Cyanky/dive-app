"""empty message

Revision ID: 10eefbf4089b
Revises: a07c821b1724
Create Date: 2022-06-05 19:48:08.969698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10eefbf4089b'
down_revision = 'a07c821b1724'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('musician', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('musician', 'genres')
    # ### end Alembic commands ###
