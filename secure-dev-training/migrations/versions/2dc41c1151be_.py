"""empty message

Revision ID: 2dc41c1151be
Revises: 6086c54a7967
Create Date: 2024-08-06 15:24:22.995854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dc41c1151be'
down_revision = '6086c54a7967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('login_code')
    # ### end Alembic commands ###