"""empty message

Revision ID: c198e4c92b20
Revises: 2dc41c1151be
Create Date: 2024-09-06 10:18:18.302671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c198e4c92b20'
down_revision = '2dc41c1151be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('challenge', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('challenge', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
