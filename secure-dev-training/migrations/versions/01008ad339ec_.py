"""empty message

Revision ID: 01008ad339ec
Revises: 7f549f63275d
Create Date: 2024-06-30 19:38:40.659100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01008ad339ec'
down_revision = '7f549f63275d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ip_addr', sa.String(), nullable=False),
    sa.Column('flag', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('challenge', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_challenge_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('challenge', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_challenge_name'))

    op.drop_table('challenge')
    # ### end Alembic commands ###
