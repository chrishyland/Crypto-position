"""Bitcoin table

Revision ID: c8542cd94b7d
Revises: 
Create Date: 2018-01-23 16:09:53.627618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8542cd94b7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bitcoin',
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('marketcap', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bitcoin')
    # ### end Alembic commands ###
